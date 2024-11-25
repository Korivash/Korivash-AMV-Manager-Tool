from tkinter import filedialog, messagebox, Toplevel, Button, Label, Scale
from moviepy.editor import AudioFileClip
import os

class AudioOperations:
    def __init__(self, controller):
        self.controller = controller

    def add_audio(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3;*.wav")])
        if file_path:
            try:
                self.controller.audio_file = AudioFileClip(file_path)
                messagebox.showinfo("Success", f"Audio track added: {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load audio file: {e}")

    def trim_audio(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3;*.wav")])
        if file_path:
            try:
                audio_clip = AudioFileClip(file_path)

                
                trim_window = Toplevel(self.controller.root)
                trim_window.title("Trim Audio")
                trim_window.geometry("400x300")

                
                Label(trim_window, text="Select Start and End Points for Trimming").pack(pady=10)
                
                
                start_scale = Scale(trim_window, from_=0, to=audio_clip.duration, orient="horizontal", length=300, label="Start Time (seconds)")
                start_scale.pack(pady=10)
                
                end_scale = Scale(trim_window, from_=0, to=audio_clip.duration, orient="horizontal", length=300, label="End Time (seconds)")
                end_scale.set(audio_clip.duration)
                end_scale.pack(pady=10)

                
                def apply_trim():
                    start_time = start_scale.get()
                    end_time = end_scale.get()
                    if start_time < end_time:
                        trimmed_audio = audio_clip.subclip(start_time, end_time)
                        self.controller.audio_file = trimmed_audio
                        messagebox.showinfo("Success", f"Trimmed audio track added from {start_time} to {end_time} seconds")
                        trim_window.destroy()
                    else:
                        messagebox.showerror("Error", "End time must be greater than start time")

                trim_button = Button(trim_window, text="Trim Audio", command=apply_trim)
                trim_button.pack(pady=20)
            
            except Exception as e:
                messagebox.showerror("Error", f"Failed to trim audio file: {e}")

