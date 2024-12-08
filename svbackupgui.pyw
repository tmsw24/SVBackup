from svbackup import pull_saves, push_saves, open_settings
import tkinter as tk
import time

def pull_button_clicked(eventlog):
    eventlog.config(text=pull_saves())

def push_button_clicked(eventlog):
    eventlog.config(text=push_saves())

def settings_button_clicked(eventlog):
    eventlog.config(text="opening settings.json")
    open_settings()

class GUI:
    def __init__(self, root, title, width, height, padding):
        self.colours = {
            "background": "#1E1E1E",
            "primary": "#FFFFFF",
            "secondary": "#00FF00"
        }
        self.padding = padding
        self.title = title
        self.width = width
        self.height = height

        self.root = root
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.config(bg=self.colours["background"])

        self.create_widgets()

    def create_label(self, text, colour, font, size, bold):
        label = tk.Label(self.root, text=text, font=(font, size, "bold" if bold else "normal"), wraplength=self.width - 20, fg=colour, bg=self.colours["background"])
        label.pack(pady=self.padding)
        return label
    
    def create_frame(self):
        frame = tk.Frame(self.root, bg=self.colours["background"])
        frame.pack(pady=self.padding)
        return frame
    
    def create_button(self, frame, text, width, height, command):
        button = tk.Button(frame, text=text, width=width, height=height, command=command)
        button.pack(side=tk.LEFT, padx=self.padding)
        return button
    
    def create_widgets(self):
        self.title = self.create_label(self.title, self.colours["primary"], "Arial", 16, True)
        self.eventlog = self.create_label("", self.colours["secondary"], "Arial", 8, False)

        self.frame1 = self.create_frame()
        self.pullbutton = self.create_button(self.frame1, "Pull Saves", 10, 1, lambda: pull_button_clicked(self.eventlog))
        self.pushbutton = self.create_button(self.frame1, "Push Saves", 10, 1, lambda: push_button_clicked(self.eventlog))

        self.frame2 = self.create_frame()
        self.settingsbutton = self.create_button(self.frame2, "Open Settings", 23, 1, lambda: settings_button_clicked(self.eventlog))

def main(title, width, height, padding):
    root = tk.Tk()
    GUI(root, title, width, height, padding)
    root.mainloop()

if __name__ == "__main__":
    main(title="Stardew Valley Backup Tool", width=400, height=200, padding=5)