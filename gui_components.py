import tkinter as tk
from tkinter import ttk, Scale

class GUIComponents:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

    def setup_components(self):
        
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", foreground="#ECEFF4", background="#4C566A", font=("Helvetica", 12), padding=10)
        style.configure("TLabel", foreground="#ECEFF4", background="#2E3440", font=("Helvetica", 14))
        style.configure("TText", foreground="#ECEFF4", background="#3B4252", font=("Helvetica", 10))
        style.configure("TFrame", background="#2E3440")

        
        self.title_label = ttk.Label(self.root, text="Korivash AMV Manager Tool", font=("Helvetica", 18, "bold"))
        self.title_label.pack(pady=20)

        
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=20)

        self.add_clip_btn = ttk.Button(button_frame, text="Add Video Clip", command=self.controller.add_clip)
        self.add_clip_btn.grid(row=0, column=0, padx=10, pady=10)
        
        self.trim_clip_btn = ttk.Button(button_frame, text="Trim & Add Clip", command=self.controller.trim_clip)
        self.trim_clip_btn.grid(row=0, column=1, padx=10, pady=10)
        
        self.add_audio_btn = ttk.Button(button_frame, text="Add Audio Track", command=self.controller.add_audio)
        self.add_audio_btn.grid(row=0, column=2, padx=10, pady=10)
        
        self.trim_audio_btn = ttk.Button(button_frame, text="Trim & Add Audio", command=self.controller.trim_audio)
        self.trim_audio_btn.grid(row=0, column=3, padx=10, pady=10)
        
        self.add_text_btn = ttk.Button(button_frame, text="Add Text Overlay", command=self.controller.add_text_overlay)
        self.add_text_btn.grid(row=0, column=4, padx=10, pady=10)
        
        self.reorder_btn = ttk.Button(button_frame, text="Reorder Clips", command=self.controller.reorder_clips)
        self.reorder_btn.grid(row=0, column=5, padx=10, pady=10)
        
        self.delete_clip_btn = ttk.Button(button_frame, text="Delete Clip", command=self.controller.delete_clip)
        self.delete_clip_btn.grid(row=0, column=6, padx=10, pady=10)
        
        self.export_btn = ttk.Button(button_frame, text="Export AMV", command=self.controller.export_amv)
        self.export_btn.grid(row=0, column=7, padx=10, pady=10)
        
        
        self.loop_var = tk.BooleanVar()
        self.loop_check = ttk.Checkbutton(self.root, text="Loop Clips", variable=self.loop_var)
        self.loop_check.pack(pady=10)
        
        
        self.clips_label = ttk.Label(self.root, text="Video Clips:")
        self.clips_label.pack(pady=5)
        
        
        self.clips_text_frame = ttk.Frame(self.root)
        self.clips_text_frame.pack(pady=5)
        self.clips_text = tk.Text(self.clips_text_frame, width=90, height=10, bg="#3B4252", fg="#ECEFF4", font=("Helvetica", 10), wrap=tk.WORD)
        self.clips_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar = ttk.Scrollbar(self.clips_text_frame, command=self.clips_text.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.clips_text.config(yscrollcommand=self.scrollbar.set)

        
        self.volume_frame = ttk.Frame(self.root)
        self.volume_frame.pack(pady=10)
        self.volume_label = ttk.Label(self.volume_frame, text="Audio Volume:")
        self.volume_label.pack(side=tk.LEFT, padx=5)
        self.volume_control = Scale(self.volume_frame, from_=0, to=100, orient=tk.HORIZONTAL, length=400, bg="#3B4252", fg="#ECEFF4")
        self.volume_control.set(100)
        self.volume_control.pack(side=tk.LEFT, padx=5)

        
        self.speed_frame = ttk.Frame(self.root)
        self.speed_frame.pack(pady=10)
        self.speed_label = ttk.Label(self.speed_frame, text="Video Speed (0.5x - 2.0x):")
        self.speed_label.pack(side=tk.LEFT, padx=5)
        self.speed_control = Scale(self.speed_frame, from_=0.5, to=2.0, resolution=0.1, orient=tk.HORIZONTAL, length=400, bg="#3B4252", fg="#ECEFF4")
        self.speed_control.set(1.0)
        self.speed_control.pack(side=tk.LEFT, padx=5)
