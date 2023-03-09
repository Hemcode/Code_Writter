from tkinter import *

# Variables and constants
PROJECT_NAME: str = "Code Writter"

white = "#ffffff"
black = "#000000"
grey = "#bbbbbb"
dark_grey = "#575656"
very_dark_grey = "#393535"

# Window
window = Tk()

window.title(PROJECT_NAME)
window.geometry("640x480")
window.minsize(480, 360)

# Frames
file_explorer_frame = Frame(window, bg=very_dark_grey)

# Label
project_name_dir = Label(file_explorer_frame, bg=black, fg=white, text="Project Dir", font=("Helvetica", 20))
project_name_dir.pack(side=TOP)

# Configure
window.config(bg=grey)

# Show objects
file_explorer_frame.pack(side="left")
window.mainloop()
