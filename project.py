# Contact Management System in Python

# Initialize an empty list to store contacts
contacts = []

def add_contact(name, phone, email):
    # Add a new contact to the list
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    print(f"Contact {name} added successfully.")

def display_contacts():
    # Display all contacts
    if not contacts:
        print("No contacts to display.")
    else:
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def update_contact(name):
    # Update a contact's details
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Contact found. Enter new details.")
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            
            contact["name"] = new_name
            contact["phone"] = new_phone
            contact["email"] = new_email
            print(f"Contact {name} updated successfully.")
            return
    print("Contact not found.")

def delete_contact(name):
    # Delete a contact by name
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print(f"Contact {name} deleted successfully.")
            return
    print("Contact not found.")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)
        
        elif choice == "2":
            display_contacts()
        
        elif choice == "3":
            name = input("Enter the name of the contact to update: ")
            update_contact(name)
        
        elif choice == "4":
            name = input("Enter the name of the contact to delete: ")
            delete_contact(name)
        
        elif choice == "5":
            print("Exiting Contact Management System.")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the contact management system
main()
