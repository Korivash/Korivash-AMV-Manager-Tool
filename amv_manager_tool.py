import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip
import threading

class KorivashAMVManagerTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Korivash AMV Manager Tool")
        self.root.geometry("600x500")
        self.root.configure(bg="#2E3440")

        
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", foreground="#ECEFF4", background="#4C566A", font=("Helvetica", 12))
        style.configure("TLabel", foreground="#ECEFF4", background="#2E3440", font=("Helvetica", 12))
        style.configure("TText", foreground="#ECEFF4", background="#3B4252", font=("Helvetica", 10))
        style.configure("TFrame", background="#2E3440")
        
        
        button_frame = ttk.Frame(root)
        button_frame.pack(pady=20)

        self.add_clip_btn = ttk.Button(button_frame, text="Add Video Clip", command=self.add_clip)
        self.add_clip_btn.grid(row=0, column=0, padx=10)
        
        self.add_audio_btn = ttk.Button(button_frame, text="Add Audio Track", command=self.add_audio)
        self.add_audio_btn.grid(row=0, column=1, padx=10)
        
        self.export_btn = ttk.Button(button_frame, text="Export AMV", command=self.export_amv)
        self.export_btn.grid(row=0, column=2, padx=10)
        
        
        self.clips_label = ttk.Label(root, text="Video Clips:")
        self.clips_label.pack(pady=5)
        
        
        self.clips_text = tk.Text(root, width=60, height=15, bg="#3B4252", fg="#ECEFF4", font=("Helvetica", 10))
        self.clips_text.pack(pady=5)

        
        self.clip_list = []
        self.clip_files = []
        self.audio_file = None

    def add_clip(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mov")])
        if file_path:
            self.clip_files.append(file_path)
            self.clip_list.append(VideoFileClip(file_path))
            self.clips_text.insert(tk.END, f"Added: {os.path.basename(file_path)}\n")

    def add_audio(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3;*.wav")])
        if file_path:
            self.audio_file = AudioFileClip(file_path)
            messagebox.showinfo("Success", f"Audio track added: {os.path.basename(file_path)}")

    def export_amv(self):
        if not self.clip_list:
            messagebox.showwarning("Warning", "No video clips added!")
            return

        export_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
        if not export_path:
            return

        
        export_thread = threading.Thread(target=self._export_amv_thread, args=(export_path,))
        export_thread.start()

    def _export_amv_thread(self, export_path):
        try:
            final_clip = concatenate_videoclips(self.clip_list)

            if self.audio_file:
                final_clip = final_clip.set_audio(self.audio_file)

            final_clip.write_videofile(export_path, codec="libx264")
            messagebox.showinfo("Export Complete", "Your AMV has been exported successfully!")
        except Exception as e:
            messagebox.showerror("Export Failed", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    amv_manager = KorivashAMVManagerTool(root)
    root.mainloop()

