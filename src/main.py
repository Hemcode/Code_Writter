"""The main file in this project"""

from tkinter import *

# importantion of other files
from openFile import File as fi
from openFolder import Folder as fl

# functions
def open_file():
    global FONT
    global grey
    global dark_grey
    global very_dark_grey

    path_entry_pop_up = Tk()
    path_entry_pop_up.config(bg=dark_grey)
    path_entry_pop_up.geometry("360x240")
    path_entry_pop_up.resizable(width=False, height=False)

    path_entry_pop_up_frame = Frame(path_entry_pop_up, bg=dark_grey)

    path_entry = Entry(path_entry_pop_up_frame, font=FONT, bg=very_dark_grey)
    path_entry.pack()

    button_entry = Button(path_entry_pop_up_frame, text="Open file", bg=grey, command=path_entry.get)
    button_entry.pack()

    file_name_path = path_entry.get().split("\\")

    file_name: str = file_name_path[-1]

    file_for_edit = fi(file_name=file_name)

    path_entry_pop_up_frame.pack(expand=YES)
    path_entry_pop_up.mainloop()

# Variable
grey: str = "#6e6e6e"
dark_grey: str = "#393939"
very_dark_grey: str = "#1a1c20"

# Font
FONT: tuple = ("Corrier", 12)


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

# Window's menu
menu_bar = Menu(window)
menu_first_option = Menu(menu_bar, tearoff=0, font=("Courrier", 12))
menu_first_option.add_command(label="Open a file", command=open_file)

menu_second_option = Menu(menu_bar, tearoff=0, font=("Courrier", 12))
menu_second_option.add_command(label="Settings")

menu_bar.add_cascade(label="Files", menu=menu_first_option)
menu_bar.add_cascade(label="Settings", menu=menu_second_option)

# Confugure
window.config(bg=grey, menu=menu_bar)

files_explore.pack(side=LEFT, fill=Y)
window.mainloop()
