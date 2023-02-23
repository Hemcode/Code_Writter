from tkinter import *

# importantion of other files
from classe.file import File
from classe.folder import Folder
from classe.fonction import *
 
# Variable
grey: str = "#6e6e6e"
dark_grey: str = "#393939"
very_dark_grey: str = "#1a1c20"


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


# Window Top
window_top = Frame(window, bg=very_dark_grey)

# Labels / Buttons

# Folder Project Name
folder_project_name = Label(files_explore_top, text="Project Name", bg=grey, font=("Courrier", 18))
folder_project_name.pack(expand=YES)

# Window Top's options
window_top_option_1 = Button(window_top, text="FILES", font=("Courrier", 11),bg=very_dark_grey, fg="white", command="")
window_top_option_1.pack(side=LEFT, padx=25)

window_top_option_2 = Button(window_top, text="SETTINGS", font=("Courrier", 11), bg=very_dark_grey, fg="white", command="")
window_top_option_2.pack(side=LEFT, padx=25)


# show elements
files_explore.pack(side=LEFT, fill=Y)
window_top.pack(side=TOP, fill=X)
window.mainloop()