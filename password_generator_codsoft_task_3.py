import random
import string
from tkinter import *
import pyperclip

# Initialize Window
root = Tk()
root.geometry("500x500")

# Title of our window
root.title("Random Password Generator")

# Random Password generator function
output_password = StringVar()
all_combinations = [string.punctuation, string.ascii_uppercase, string.digits, string.ascii_lowercase]

def generate_password():
    password = ""
    for _ in range(password_length.get()):
        char_type = random.choice(all_combinations)
        password = password + random.choice(char_type)
    output_password.set(password)

# Copy to clipboard function
def copy_password():
    pyperclip.copy(output_password.get())

# Front-end Designing (GUI)
password_heading = Label(root, text='Password Length', font='Arial 12 bold', bg='lightblue').pack(pady=10)

password_length = IntVar()
password_spinbox = Spinbox(root, from_=4, to_=32, textvariable=password_length, width=24, font='arial 16').pack()

# Generate password button
generate_button = Button(root, command=generate_password, text="Generate Password", font="Arial 10", bg='lightgreen', fg='black', activebackground="teal", padx=5, pady=5).pack(pady=20)

password_label = Label(root, text='Random Generated Password', font='arial 12 bold', bg='lightblue').pack(pady="30 10")
password_entry = Entry(root, textvariable=output_password, width=24, font='arial 16').pack()

# Copy to clipboard button
copy_button = Button(root, text='Copy to Clipboard', command=copy_password, font="Arial 10", bg='light yellow', fg='black', activebackground="teal", padx=5, pady=5).pack(pady=20)

root.mainloop()
