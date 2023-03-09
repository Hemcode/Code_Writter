from tkinter import Tk, Entry, Menu, Button, Frame, Label

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

# Configure
window.config(bg=grey)

# Show objects
window.mainloop()