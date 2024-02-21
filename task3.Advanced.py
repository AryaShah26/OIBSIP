import random
import string
from tkinter import *
from tkinter import messagebox

def generate_password():
    password_length = int(length_entry.get())
    character_types = [char for char in "lnss" if char in character_types_var.get()]

    if not character_types:
        messagebox.showerror("Error", "Please select at least one character type.")
        return

    character_sets = {
        "l": string.ascii_letters,
        "n": string.digits,
        "s": string.punctuation
    }

    password_characters = "".join(character_sets[char_type] for char_type in character_types)

    password = generate_password_with_rules(password_length, password_characters)
    password_entry.delete(0, END)
    password_entry.insert(0, password)


def generate_password_with_rules(length, characters):
    password = []

    if "l" in characters:
        password.append(random.choice(string.ascii_uppercase))

    if "n" in characters:
        password.append(random.choice(string.digits))

    if "s" in characters:
        password.append(random.choice(string.punctuation))

    for _ in range(length - len(password)):
        password.append(random.choice(characters))

    random.shuffle(password)

    return "".join(password)


def copy_password():
    password = password_entry.get()
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Success", "Password copied to clipboard.")


root = Tk()
root.title("Password Generator")

frame = Frame(root)
frame.pack(padx=10, pady=10)

length_label = Label(frame, text="Password length:")
length_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

length_entry = Entry(frame, width=5)
length_entry.grid(row=0, column=1, padx=5, pady=5)

character_types_label = Label(frame, text="Character types:")
character_types_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

character_types_var = StringVar()
character_types_checkboxes = [Checkbutton(frame, text=char_type, variable=character_types_var, onvalue=char_type, offvalue="") for char_type in "lnss"]
for i, checkbox in enumerate(character_types_checkboxes):
    checkbox.grid(row=1, column=i + 1, padx=5, pady=5)

generate_button = Button(frame, text="Generate", command=generate_password)
generate_button.grid(row=2, column=0, padx=5, pady=5)

password_label = Label(frame, text="Generated password:")
password_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)

password_entry = Entry(frame, width=50)
password_entry.grid(row=3, column=1, padx=5, pady=5)

copy_button = Button(frame, text="Copy", command=copy_password)
copy_button.grid(row=3, column=2, padx=5, pady=5)

root.mainloop()