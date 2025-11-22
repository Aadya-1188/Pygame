# import necesaary libraries
from tkinter import *
from datetime import date

# create window
root = Tk()
root.title("Getting started with widgets")
root.geometry("400x300")

# add widgets
# add label
lbl = Label(text = "Heyyy!", fg="white", bg="#61212D", height=1, width = 30 )

# add label for getting name from user
name_lbl = Label(text = "Whats your name?", bg="#DBB2B9", fg="#61212D")
name_entry = Entry()

# function to display a message
def display():
    # read input by user
    name = name_entry.get()
    # declare a global variable
    # global variable can be used outside this function
    global message
    message = "Welcome to the app! \n todays date is:"
    greet = "Hello "+ name+"\n"
    # display details in a textox
    # specify where to add details in the tect box
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

# ADD A TEXT WIDGET TO DISPLAY TEXT
text_box = Text(height=3)

# add a button and give value of command to execute function
btn = Button(text="display", command=display, bg="#61212D", fg="white")

# oragnize widgets in the window
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

# start the main loop
root.mainloop()