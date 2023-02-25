from tkinter import *

# Variable
font_tuple = ("Corrier", 22)

# Function for open file
def open_file(file_name: str, window: Tk):
    file_object = open(file_name, "r+")
    
    entry_frame = Frame(window, bg="#393939") # Dark Grey

    file_entry = Entry(entry_frame, font=("Corrier", 12), fg="black")
    file_entry.pack()

    entry_frame.pack(expand=YES)


# Function for open a pop-up to chose the file to open.
def pop_up_for_open_file(window: Tk):
    pop_up = Tk()
    pop_up.title("Chose a file")
    pop_up.config(bg="#6e6e6e") # Grey

    pop_up_frame = Frame(pop_up, bg="#393939") # Dark Grey

    path_entry = Entry(pop_up_frame, font=("Courrier", 25), bg="#1a1c20") # Very dark grey
    path_entry.pack()

    path_register = Button(pop_up_frame, text="Entrer the file's path for open it", bg="#48577d", fg="white", command=open_file(path_entry, window))
    path_register.pack()

    # Show the pop-up
    pop_up_frame.pack(expand=YES)
    pop_up.mainloop()


def we_are_sorry():
    sorry_pop_up = Tk()
    sorry_pop_up.geometry("720x480")
    sorry_pop_up.resizable(height=False, width=False)
    sorry_pop_up.title("We're sorry")
    sorry_pop_up.config(bg="#1a1c20") # Very Dark Grey

    sorry_message = Label(sorry_pop_up, text="We're sorry, this functionality isn't programmed.", font=font_tuple, bg="#1a1c20", fg="white") # Very Dark Grey
    sorry_message.pack(expand=YES)

    sorry_pop_up.mainloop()