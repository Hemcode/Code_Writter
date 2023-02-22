from tkinter import *

# Variable
grey: str = "#6e6e6e"
dark_grey: str = "#393939"
very_dark_grey: str = "#1a1c20"

# Window
window = Tk()

window.title = "Code Writter"
window.config(bg=grey)
window.minsize(480, 360)
window.geometry("1080x720")
window.iconbitmap("cw.ico")


# mainloop
window.mainloop()