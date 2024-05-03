import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, sapid, course, address, phone_number, city, favorite=False):
        self.name = name
        self.sapid = sapid
        self.course = course
        self.address = address
        self.phone_number = phone_number
        self.city = city
        self.favorite = favorite

class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, sapid, course, address, phone_number, city):
        if name.lower() in self.contacts:
            messagebox.showwarning("Warning", f"Contact {name} already exists.")
        else:
            contact = Contact(name, sapid, course, address, phone_number, city)
            self.contacts[name.lower()] = contact

    def delete_contact(self, name):
        if name.lower() in self.contacts:
            del self.contacts[name.lower()]
        else:
            messagebox.showwarning("Warning", f"Contact {name} not found.")

    def search_contact(self, name):
        contact = self.contacts.get(name.lower())
        if contact:
            messagebox.showinfo("Contact Info", f"Name: {contact.name}\nSAP ID: {contact.sapid}\nCourse: {contact.course}\nAddress: {contact.address}\nCity: {contact.city}\nPhone Number: {contact.phone_number}")
        else:
            messagebox.showwarning("Warning", f"Contact {name} not found.")

    def list_contacts(self):
        if self.contacts:
            contact_list = "\n".join([contact.name for contact in self.contacts.values()])
            messagebox.showinfo("Contacts", f"Contacts:\n{contact_list}")
        else:
            messagebox.showinfo("Info", "Address book is empty.")

    def add_favorite(self, name):
        contact = self.contacts.get(name.lower())
        if contact:
            contact.favorite = True
            messagebox.showinfo("Info", f"{contact.name} added to favorites.")
        else:
            messagebox.showwarning("Warning", f"Contact {name} not found.")

    def list_favorites(self):
        favorites = [contact.name for contact in self.contacts.values() if contact.favorite]
        if favorites:
            favorite_list = "\n".join(favorites)
            messagebox.showinfo("Favorites", f"Favorites:\n{favorite_list}")
        else:
            messagebox.showinfo("Info", "No favorites found.")

class AddressBookApp:
    def __init__(self, master):
        self.master = master
        master.title("Address Book")
        master.geometry("400x400")
        master.configure(bg="#f0f0f0")

        self.address_book = AddressBook()

        self.label = tk.Label(master, text="Address Book Menu", font=("Helvetica", 16), bg="#f0f0f0")
        self.label.pack(pady=10)

        buttons_frame = tk.Frame(master, bg="#f0f0f0")
        buttons_frame.pack()

        self.add_button = tk.Button(buttons_frame, text="Add Contact", command=self.add_contact, font=("Helvetica", 12))
        self.add_button.grid(row=0, column=0, padx=5, pady=5)

        self.delete_button = tk.Button(buttons_frame, text="Delete Contact", command=self.delete_contact, font=("Helvetica", 12))
        self.delete_button.grid(row=0, column=1, padx=5, pady=5)

        self.search_button = tk.Button(buttons_frame, text="Search Contact", command=self.search_contact, font=("Helvetica", 12))
        self.search_button.grid(row=0, column=2, padx=5, pady=5)

        self.list_button = tk.Button(buttons_frame, text="List Contacts", command=self.list_contacts, font=("Helvetica", 12))
        self.list_button.grid(row=1, column=0, padx=5, pady=5)

        self.add_fav_button = tk.Button(buttons_frame, text="Add to Favorites", command=self.add_favorite, font=("Helvetica", 12))
        self.add_fav_button.grid(row=1, column=1, padx=5, pady=5)

        self.list_fav_button = tk.Button(buttons_frame, text="List Favorites", command=self.list_favorites, font=("Helvetica", 12))
        self.list_fav_button.grid(row=1, column=2, padx=5, pady=5)

        self.exit_button = tk.Button(master, text="Exit", command=master.quit, font=("Helvetica", 12))
        self.exit_button.pack(pady=10)

    def add_contact(self):
        self.add_window = tk.Toplevel(self.master)
        self.add_window.title("Add Contact")
        self.add_window.geometry("300x250")
        self.add_window.configure(bg="#f0f0f0")

        tk.Label(self.add_window, text="Name:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.add_window, text="SAP ID:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.add_window, text="Course:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=2, column=0, padx=5, pady=5)
        tk.Label(self.add_window, text="Address:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=3, column=0, padx=5, pady=5)
        tk.Label(self.add_window, text="Phone Number:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=4, column=0, padx=5, pady=5)
        tk.Label(self.add_window, text="City:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=5, column=0, padx=5, pady=5)

        self.name_entry = tk.Entry(self.add_window)
        self.sapid_entry = tk.Entry(self.add_window)
        self.course_entry = tk.Entry(self.add_window)
        self.address_entry = tk.Entry(self.add_window)
        self.phone_entry = tk.Entry(self.add_window)
        self.city_entry = tk.Entry(self.add_window)

        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.sapid_entry.grid(row=1, column=1, padx=5, pady=5)
        self.course_entry.grid(row=2, column=1, padx=5, pady=5)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)
        self.phone_entry.grid(row=4, column=1, padx=5, pady=5)
        self.city_entry.grid(row=5, column=1, padx=5, pady=5)

        tk.Button(self.add_window, text="Add", command=self.add_contact_action, font=("Helvetica", 12)).grid(row=6, column=0, columnspan=2, padx=5, pady=10)

    def add_contact_action(self):
        name = self.name_entry.get()
        sapid = self.sapid_entry.get()
        course = self.course_entry.get()
        address = self.address_entry.get()
        phone_number = self.phone_entry.get()
        city = self.city_entry.get()

        self.address_book.add_contact(name, sapid, course, address, phone_number, city)
        messagebox.showinfo("Success", f"Contact {name} added successfully!")

        self.add_window.destroy()

    def delete_contact(self):
        self.delete_window = tk.Toplevel(self.master)
        self.delete_window.title("Delete Contact")
        self.delete_window.geometry("250x100")
        self.delete_window.configure(bg="#f0f0f0")

        tk.Label(self.delete_window, text="Name:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=0, column=0, padx=5, pady=5)

        self.delete_name_entry = tk.Entry(self.delete_window)
        self.delete_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(self.delete_window, text="Delete", command=self.delete_contact_action, font=("Helvetica", 12)).grid(row=1, column=0, columnspan=2, padx=5, pady=10)

    def delete_contact_action(self):
        name = self.delete_name_entry.get()
        self.address_book.delete_contact(name)

        self.delete_window.destroy()

    def search_contact(self):
        self.search_window = tk.Toplevel(self.master)
        self.search_window.title("Search Contact")
        self.search_window.geometry("250x100")
        self.search_window.configure(bg="#f0f0f0")

        tk.Label(self.search_window, text="Name:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=0, column=0, padx=5, pady=5)

        self.search_name_entry = tk.Entry(self.search_window)
        self.search_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(self.search_window, text="Search", command=self.search_contact_action, font=("Helvetica", 12)).grid(row=1, column=0, columnspan=2, padx=5, pady=10)

    def search_contact_action(self):
        name = self.search_name_entry.get()
        self.address_book.search_contact(name)

        self.search_window.destroy()

    def list_contacts(self):
        self.address_book.list_contacts()

    def add_favorite(self):
        self.add_fav_window = tk.Toplevel(self.master)
        self.add_fav_window.title("Add to Favorites")
        self.add_fav_window.geometry("250x100")
        self.add_fav_window.configure(bg="#f0f0f0")

        tk.Label(self.add_fav_window, text="Name:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=0, column=0, padx=5, pady=5)

        self.add_fav_name_entry = tk.Entry(self.add_fav_window)
        self.add_fav_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(self.add_fav_window, text="Add", command=self.add_favorite_action, font=("Helvetica", 12)).grid(row=1, column=0, columnspan=2, padx=5, pady=10)

    def add_favorite_action(self):
        name = self.add_fav_name_entry.get()
        self.address_book.add_favorite(name)

        self.add_fav_window.destroy()

    def list_favorites(self):
        self.address_book.list_favorites()

def main():
    root = tk.Tk()
    app = AddressBookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
