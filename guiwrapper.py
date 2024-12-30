from svbackup import pull_saves, push_saves, open_settings, fix_ui
from tkinter import filedialog
import tkinter as tk

def pull_button_clicked(eventlog):
    output = pull_saves()
    eventlog.config(text=output.stdout if output.stdout else output.stderr)

def push_button_clicked(eventlog):
    output = push_saves()
    eventlog.config(text=output.stdout if output.stdout else output.stderr)

def settings_button_clicked(eventlog):
    eventlog.config(text="opening settings.json")
    open_settings()

def fix_ui_button_clicked(eventlog):
    savefile = filedialog.askopenfilename(
        title="Select the main Stardew Valley save file (e.g farmname_123456789)",
        filetypes=[("All Files", "*.*")]
    )
    if savefile:
        fix_ui(savefile)
        eventlog.config(text="ui fixed")

class GUI:
    def __init__(self, root, type, title, width, height, padding):
        self.colours = {
            "background": "#1E1E1E",
            "primary": "#FFFFFF",
            "secondary": "#00FF00"
        }
        self.type = type
        self.title = title
        self.width = width
        self.height = height
        self.padding = padding

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
        match self.type:
            case "svbackupgui.pyw":
                self.title = self.create_label(self.title, self.colours["primary"], "Arial", 16, True)
                self.eventlog = self.create_label("", self.colours["secondary"], "Arial", 8, False)
                
                self.frame1 = self.create_frame()
                self.pullbutton = self.create_button(self.frame1, "Pull Saves", 10, 1, lambda: pull_button_clicked(self.eventlog))
                self.pushbutton = self.create_button(self.frame1, "Push Saves", 10, 1, lambda: push_button_clicked(self.eventlog))
                
                self.frame2 = self.create_frame()
                self.settingsbutton = self.create_button(self.frame2, "Open Settings", 23, 1, lambda: settings_button_clicked(self.eventlog))
            case "fixui.pyw":
                self.title = self.create_label(self.title, self.colours["primary"], "Arial", 16, True)
                self.eventlog = self.create_label("", self.colours["secondary"], "Arial", 8, False)

                self.frame = self.create_frame()
                self.fixuibutton = self.create_button(self.frame, "Fix UI", 10, 1, lambda: fix_ui_button_clicked(self.eventlog))