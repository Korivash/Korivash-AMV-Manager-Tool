import os
from tkinter import filedialog, messagebox, simpledialog
from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx, CompositeVideoClip
import threading

class VideoOperations:
    def __init__(self, controller):
        self.controller = controller

    def add_clip(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mov")])
        if file_path:
            try:
                clip = VideoFileClip(file_path).resize(height=720)  # Ensure consistent resolution
                self.controller.clip_files.append(file_path)
                self.controller.clip_list.append(clip)
                self.controller.gui.clips_text.insert("end", f"Added: {os.path.basename(file_path)}\n")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load video file: {e}")

    def trim_clip(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mov")])
        if file_path:
            start_time_str = simpledialog.askstring("Trim Start", "Enter start time (MM:SS or HH:MM:SS):")
            end_time_str = simpledialog.askstring("Trim End", "Enter end time (MM:SS or HH:MM:SS):")
            start_time = self.controller.utils.convert_time_to_seconds(start_time_str)
            end_time = self.controller.utils.convert_time_to_seconds(end_time_str)
            if start_time is not None and end_time is not None:
                try:
                    clip = VideoFileClip(file_path).subclip(start_time, end_time).resize(height=720)
                    self.controller.clip_files.append(file_path)
                    self.controller.clip_list.append(clip)
                    self.controller.gui.clips_text.insert("end", f"Added (trimmed): {os.path.basename(file_path)} from {start_time_str} to {end_time_str}\n")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to trim video file: {e}")

    def reorder_clips(self):
        if len(self.controller.clip_list) < 2:
            messagebox.showwarning("Warning", "Not enough clips to reorder.")
            return

        current_order = "\n".join([f"{i + 1}. {os.path.basename(clip_file)}" for i, clip_file in enumerate(self.controller.clip_files)])
        new_order = simpledialog.askstring("Reorder Clips", f"Current Order:\n{current_order}\nEnter new order as comma-separated indices (e.g., 2,1,3):")
        if new_order:
            try:
                new_indices = [int(i.strip()) - 1 for i in new_order.split(",")]
                if len(new_indices) != len(self.controller.clip_list) or any(i < 0 or i >= len(self.controller.clip_list) for i in new_indices):
                    raise ValueError
                self.controller.clip_list = [self.controller.clip_list[i] for i in new_indices]
                self.controller.clip_files = [self.controller.clip_files[i] for i in new_indices]
                self.controller.gui.clips_text.delete(1.0, "end")
                for i, clip_file in enumerate(self.controller.clip_files):
                    self.controller.gui.clips_text.insert("end", f"{i + 1}. {os.path.basename(clip_file)}\n")
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter valid indices.")

    def delete_clip(self):
        if not self.controller.clip_list:
            messagebox.showwarning("Warning", "No clips to delete.")
            return

        current_order = "\n".join([f"{i + 1}. {os.path.basename(clip_file)}" for i, clip_file in enumerate(self.controller.clip_files)])
        clip_to_delete = simpledialog.askinteger("Delete Clip", f"Current Clips:\n{current_order}\nEnter the number of the clip to delete:")
        if clip_to_delete is not None:
            try:
                index = clip_to_delete - 1
                if index < 0 or index >= len(self.controller.clip_list):
                    raise ValueError
                del self.controller.clip_list[index]
                del self.controller.clip_files[index]
                self.controller.gui.clips_text.delete(1.0, "end")
                for i, clip_file in enumerate(self.controller.clip_files):
                    self.controller.gui.clips_text.insert("end", f"{i + 1}. {os.path.basename(clip_file)}\n")
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter a valid clip number.")

    def export_amv(self):
        if not self.controller.clip_list:
            messagebox.showwarning("Warning", "No video clips added!")
            return

        export_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
        if not export_path:
            return

        
        export_thread = threading.Thread(target=self._export_amv_thread, args=(export_path,))
        export_thread.start()

    def _export_amv_thread(self, export_path):
        try:
            final_clips = []
            for clip in self.controller.clip_list:
                
                speed = self.controller.gui.speed_control.get()
                adjusted_clip = clip.fx(vfx.speedx, speed)
                adjusted_clip = adjusted_clip.resize(height=720)  # Ensure consistent resolution
                final_clips.append(adjusted_clip)

            
            total_clip_duration = sum([clip.duration for clip in final_clips])

            
            if self.controller.gui.loop_var.get() and self.controller.audio_file:
                while total_clip_duration < self.controller.audio_file.duration:
                    final_clips.extend([clip.copy() for clip in self.controller.clip_list])
                    total_clip_duration = sum([clip.duration for clip in final_clips])

            
            final_clip = concatenate_videoclips(final_clips, method="compose")  

            
            if self.controller.audio_file and final_clip.duration < self.controller.audio_file.duration:
                self.controller.audio_file = self.controller.audio_file.subclip(0, final_clip.duration)

            
            if self.controller.audio_file:
                volume = self.controller.gui.volume_control.get() / 100.0
                adjusted_audio = self.controller.audio_file.volumex(volume)
                final_clip = final_clip.set_audio(adjusted_audio)

            
            if self.controller.text_overlays:
                final_clip = CompositeVideoClip([final_clip] + self.controller.text_overlays)

            final_clip.write_videofile(export_path, codec="libx264", preset="ultrafast")
            messagebox.showinfo("Export Complete", "Your AMV has been exported successfully!")
        except Exception as e:
            messagebox.showerror("Export Failed", f"An error occurred: {str(e)}")


