"""The main file in this project"""

from tkinter import *

# importantion of other files
from include.file import File as fi

# Variable
grey: str = "#6e6e6e"
dark_grey: str = "#393939"
very_dark_grey: str = "#1a1c20"

font_tuple: tuple = ("Corrier", 11)


# Window
window = Tk()

window.title("Code Writter")

window.config(bg=grey)

window.minsize(480, 360)
window.geometry("1080x720")


# Files
files_explore = Frame(window, bg=dark_grey)
files_explore_top = Frame(files_explore, bg=very_dark_grey)
files_explore_top.pack(side=TOP)


# Labels / Buttons

# Folder Project Name
folder_project_name = Label(files_explore_top, text="Project Name", bg=grey, font=("Courrier", 18))
folder_project_name.pack(expand=YES)

# shows elements

# Window Top
window_top_menu_bar = Menu(window)
window_top_element_1 = Menu(window_top_menu_bar, tearoff=0, font=("Courrier", 12))
window_top_element_1.add_command(label="Open a file")

window_top_element_2 = Menu(window_top_menu_bar, tearoff=0, font=("Courrier", 12))
window_top_element_2.add_command(label="Settings")

window_top_menu_bar.add_cascade(label="Files", menu=window_top_element_1)
window_top_menu_bar.add_cascade(label="Settings", menu=window_top_element_2)

# Confugure
window.config(bg=grey, menu=window_top_menu_bar)

files_explore.pack(side=LEFT, fill=Y)
window.mainloop()