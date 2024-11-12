from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
        
# password = ""
# for char in password_list:
#   password += char
# print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    
    website = website_input.get()
    email = user_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Upddating old data with new data
            data.update(new_data)
            
            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_input.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        try:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title="Search", message=f"Email: {email}\nPassword: {password}")
        except KeyError:
            messagebox.showinfo(title="Error", message=f"No deatils for {website} exists.")
            
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website:")
user_label = Label(text="Email/Username:")
password_label = Label(text="Password:")
website_label.grid(column=0, row=1)
user_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

#Entries
website_input = Entry(width=35)
user_input = Entry(width=35)
password_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
user_input.grid(column=1, row=2, columnspan=2)
password_input.grid(column=1, row=3, columnspan=2)
user_input.insert(0, "example@gmail.com")

#Buttons
generate_button = Button(text="Generate Password", width=10, command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=33, command=save)
add_button.grid(column=1, row=4, columnspan=2)
website_button = Button(text="Search", width=10, command=find_password)
website_button.grid(column=2, row=1)

window.mainloop()