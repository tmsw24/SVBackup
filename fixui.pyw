from guiwrapper import GUI, tk
import os

def main(type, title, width, height, padding):
    root = tk.Tk()
    GUI(root, type, title, width, height, padding)
    root.mainloop()

if __name__ == "__main__":
    main(type=os.path.basename(__file__), title="Stardew Valley UI Fix Tool", width=400, height=150, padding=5)