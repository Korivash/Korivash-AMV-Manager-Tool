import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk, Scale, simpledialog
from ttkthemes import ThemedTk
from video_operations import VideoOperations
from audio_operations import AudioOperations
from gui_components import GUIComponents
from utils import Utils

class KorivashAMVManagerTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Korivash AMV Manager Tool")
        self.root.geometry("1200x800")
        self.root.configure(bg="#2E3440")

       
        self.gui = GUIComponents(root, self)
        self.gui.setup_components()

        
        self.video_operations = VideoOperations(self)
        self.audio_operations = AudioOperations(self)

        
        self.clip_list = []
        self.clip_files = []
        self.audio_file = None
        self.text_overlays = []

    def add_clip(self):
        self.video_operations.add_clip()

    def trim_clip(self):
        self.video_operations.trim_clip()

    def add_audio(self):
        self.audio_operations.add_audio()

    def trim_audio(self):
        self.audio_operations.trim_audio()

    def add_text_overlay(self):
        text = simpledialog.askstring("Add Text Overlay", "Enter the text to overlay:")
        start_time_str = simpledialog.askstring("Text Start Time", "Enter start time (MM:SS or HH:MM:SS):")
        duration_str = simpledialog.askstring("Text Duration", "Enter duration in seconds:")
        start_time = Utils.convert_time_to_seconds(start_time_str)
        duration = float(duration_str) if duration_str else None
        if text and start_time is not None and duration is not None:
            try:
                text_clip = TextClip(text, fontsize=24, color='white').set_position('center').set_start(start_time).set_duration(duration)
                self.text_overlays.append(text_clip)
                messagebox.showinfo("Success", f"Text overlay added: '{text}' from {start_time_str} for {duration_str}s")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to add text overlay: {e}")

    def reorder_clips(self):
        self.video_operations.reorder_clips()

    def delete_clip(self):
        self.video_operations.delete_clip()

    def export_amv(self):
        self.video_operations.export_amv()

if __name__ == "__main__":
    root = ThemedTk(theme="equilux")
    amv_manager = KorivashAMVManagerTool(root)
    root.mainloop()
