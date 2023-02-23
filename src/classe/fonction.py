from tkinter import *

# Function for take the file name

# Function for open a pop-up to chose the file to open.
def pop_up_for_open_file():
    pop_up = Tk()
    pop_up.title("Chose a file")
    pop_up.config(bg="#6e6e6e") # Grey

    pop_up_frame = Frame(pop_up, bg="#393939") # Dark Grey

    path_entry = Entry(pop_up_frame, font=("Courrier", 25), bg="#1a1c20") # Very dark grey
    path_entry.pack()

    path_register = Button(pop_up_frame, text="Entrer the file's path for open it", command="")
    path_register.pack()

    # Show the pop-up
    pop_up_frame.pack(expand=YES, fill=Y, fill=X)
    pop_up.mainloop()


# Fuction for open a file
""" For Later
def open_file(file_name: str):
    file_object = open(file_name, "r+")

    text_entry_for_code = Entry()

    for lignes in file_object:
        return lignes
"""