



# Installs
# pip install pyautogui opencv-python

import tkinter as tk
import threading
import pyautogui
import cv2
from tkinter import filedialog
import numpy as np


class ScreenRecorderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Screen Recorder")

        self.start_button = tk.Button(root, text="Start Recording", command=self.start_recording)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Stop Recording", command=self.stop_recording)
        self.stop_button.pack()

        self.recording = False

    def start_recording(self):
        self.recording = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        self.record_thread = threading.Thread(target=self.record_screen)
        self.record_thread.start()

    def stop_recording(self):
        self.recording = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def record_screen(self):
        screen_size = pyautogui.size()
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        output_filename = filedialog.asksaveasfilename(defaultextension=".avi", filetypes=[("AVI files", "*.avi")])
        if output_filename:
            out = cv2.VideoWriter(output_filename, fourcc, 20.0, screen_size)

            while self.recording:
                screenshot = pyautogui.screenshot()
                frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
                out.write(frame)

            out.release()

root = tk.Tk()
app = ScreenRecorderApp(root)
root.mainloop()
