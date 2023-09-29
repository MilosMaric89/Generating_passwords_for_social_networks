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
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# for char in range(nr_letters):
#   password_list.append(random.choice(letters))

# for char in range(nr_symbols):
#   password_list += random.choice(symbols)

# for char in range(nr_numbers):
#   password_list += random.choice(numbers)

# password = ""
# for char in password_list:
#   password += char

# print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    #Moze i ovako da se uradi
    # if len(webiste_entry.get()) == 0 or len(password_entry.get()) == 0:
    #     messagebox.showinfo(title="error", message="Please don't let entry empty")
    new_data = {
        webiste_entry.get(): {
            "email":email_entry.get(),
            "password": password_entry.get(),
        },
    }
    if webiste_entry.get() == "":
        messagebox.showinfo(title="error", message="Please don't let entry empty")
    elif password_entry.get() == "":
        messagebox.showinfo(title="error", message="Please don't let entry empty")
    else:
        # is_ok = messagebox.askokcancel(title=f"{webiste_entry.get()}", message=f"These are the details entered: \n"
        #                                                            f"Email: {email_entry.get()}\n"
        #                                                            f"Password: {password_entry.get()}\n"
        #                                                            f"Is it ok to save?")
        # if is_ok:
        try:
            with open("data.json", mode="r") as file:
                # file.write(f"{webiste_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
                #read old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            #write new data and hold old data
            data.update(new_data)

            with open("data.json", mode="w") as file:
                #saving update data
                json.dump(data, file, indent=4)
        finally:
            webiste_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD -------------------------- #
def find_password():
    website = webiste_entry.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Your password: {password}\nYour email: {email}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Menager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
password_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

webiste_entry = Entry(width=34)
webiste_entry.grid(column=1, row=1)
webiste_entry.focus()

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

email_entry = Entry(width=53)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "mrmacmilos@gmail.com")

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

password_entry = Entry(width=34)
password_entry.grid(column=1, row=3)

password_button = Button(text="Password Generate", command=generate_password)
password_button.grid(column=2, row=3)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)

add_button = Button(width=45, text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
