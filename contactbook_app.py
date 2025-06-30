import json
import os

CONTACTS_FILE = "contacts.json"

# Load contacts from file if exists
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add new contact
def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    contacts[name] = {"Phone": phone, "Email": email}
    print(f"Contact '{name}' added successfully.")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for name, info in contacts.items():
        print(f"\nName: {name}\nPhone: {info['Phone']}\nEmail: {info['Email']}")

# Search contact
def search_contact(contacts):
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(f"Name: {name}\nPhone: {contacts[name]['Phone']}\nEmail: {contacts[name]['Email']}")
    else:
        print("Contact not found.")

# Delete contact
def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print("Contact not found.")

# Main program
def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()