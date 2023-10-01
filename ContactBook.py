import json

# Initialize an empty list to store contacts
contacts = []

# Load existing contacts from a JSON file if it exists


def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            contacts.extend(json.load(file))
    except FileNotFoundError:
        pass

# Save the current list of contacts to a JSON file


def save_contacts():
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file)

# Function to add a new contact


def add_contact():
    print("\nAdd Contact")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Address": address
    }

    contacts.append(contact)
    save_contacts()
    print(f"{name} has been added to your contacts.")

# Function to display a list of all contacts


def view_contacts():
    print("\nView Contact List")
    if not contacts:
        print("Your contact list is empty.")
    else:
        for index, contact in enumerate(contacts, start=1):
            print(
                f"{index}. Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}, Address: {contact['Address']}")

# Function to search for a contact by name or phone number


def search_contact():
    print("\nSearch Contact")
    search_query = input("Enter name or phone number to search: ")

    found_contacts = []

    for contact in contacts:
        if search_query.lower() in contact['Name'].lower() or search_query in contact['Phone']:
            found_contacts.append(contact)

    if found_contacts:
        print("Matching Contacts:")
        for index, contact in enumerate(found_contacts, start=1):
            print(
                f"{index}. Name: {contact['Name']}, Phone: {contact['Phone']}")
    else:
        print("No matching contacts found.")

# Function to update a contact


def update_contact():
    view_contacts()
    if not contacts:
        return

    choice = int(input("Enter the number of the contact to update: "))
    if 1 <= choice <= len(contacts):
        contact = contacts[choice - 1]
        print(f"Editing Contact: {contact['Name']}")
        contact['Name'] = input("Enter Updated Name: ")
        contact['Phone'] = input("Enter Updated Phone Number: ")
        contact['Email'] = input("Enter Updated Email: ")
        contact['Address'] = input("Enter Updated Address: ")
        save_contacts()
        print("Contact updated successfully.")
    else:
        print("Invalid choice. Please select a valid contact.")

# Function to delete a contact


def delete_contact():
    view_contacts()
    if not contacts:
        return

    choice = int(input("Enter the number of the contact to delete: "))
    if 1 <= choice <= len(contacts):
        contact = contacts.pop(choice - 1)
        save_contacts()
        print(f"{contact['Name']} has been deleted from your contacts.")
    else:
        print("Invalid choice. Please select a valid contact.")

# Main menu for the Contact Book


def main():
    load_contacts()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    print("Welcome to the Contact Book!")
    main()
