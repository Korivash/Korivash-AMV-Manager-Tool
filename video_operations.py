import os
from tkinter import filedialog, messagebox, simpledialog
from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx, CompositeVideoClip, AudioFileClip, concatenate_audioclips
import threading

class VideoOperations:
    def __init__(self, controller):
        self.controller = controller

    def add_clip(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mov")])
        if file_path:
            try:
                clip = VideoFileClip(file_path)
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
                    clip = VideoFileClip(file_path).subclip(start_time, end_time)
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

        # Run export in a separate thread to avoid freezing the GUI
        export_thread = threading.Thread(target=self._export_amv_thread, args=(export_path,))
        export_thread.start()

    def _export_amv_thread(self, export_path):
        try:
            final_clips = []
            for clip in self.controller.clip_list:
                # Adjust the speed of each clip based on user input
                speed = self.controller.gui.speed_control.get()
                adjusted_clip = clip.fx(vfx.speedx, speed)
                adjusted_clip = adjusted_clip.set_fps(30)  # Set a consistent frame rate to avoid playback issues
                final_clips.append(adjusted_clip)

            # Concatenate all video clips
            final_clip = concatenate_videoclips(final_clips, method="compose")

            # Set audio with volume adjustment if an audio track is added
            if self.controller.audio_file:
                # Extend audio if it is shorter than the video
                if self.controller.audio_file.duration < final_clip.duration:
                    num_loops = int(final_clip.duration // self.controller.audio_file.duration) + 1
                    extended_audio = concatenate_audioclips([self.controller.audio_file] * num_loops)  # Repeat the audio to match the video length
                    extended_audio = extended_audio.subclip(0, final_clip.duration)
                else:
                    extended_audio = self.controller.audio_file.subclip(0, final_clip.duration)
                
                volume = self.controller.gui.volume_control.get() / 100.0
                adjusted_audio = extended_audio.volumex(volume)
                final_clip = final_clip.set_audio(adjusted_audio)

            # Add text overlays
            if self.controller.text_overlays:
                final_clip = CompositeVideoClip([final_clip] + self.controller.text_overlays)

            # Export the final video with both video and audio
            final_clip.write_videofile(export_path, codec="libx264", preset="medium", fps=30, audio_codec="aac", threads=4)
            messagebox.showinfo("Export Complete", "Your AMV has been exported successfully!")
        except Exception as e:
            messagebox.showerror("Export Failed", f"An error occurred: {str(e)}")







