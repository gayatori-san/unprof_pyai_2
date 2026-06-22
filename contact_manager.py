print("====================================")
print("DIAGNOSTIC: Python has successfully opened the file!")
print("====================================")

import json
import os

FILE_NAME = "contacts.json"

def load_contacts():
    """Loads contacts from the JSON file. Returns an empty dict if it doesn't exist."""
    if not os.path.exists(FILE_NAME):
        return {}
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except Exception:
        # If the file is corrupted or empty, start with a fresh dictionary
        return {}

def save_contacts(contacts):
    """Saves the dictionary to the JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

def main():
    print("\n--- Welcome to the Contact Manager CLI ---")
    contacts = load_contacts()

    while True:
        print("\n[ Menu ]")
        print("1. Add a new contact")
        print("2. Search for a contact")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            name = input("Enter contact name: ").strip()
            phone = input("Enter phone number: ").strip()
            if name and phone:
                contacts[name] = phone
                save_contacts(contacts)
                print(f"✔️ Successfully saved {name}!")
            else:
                print("❌ Name and phone cannot be empty.")

        elif choice == "2":
            search_name = input("Enter name to search: ").strip()
            if search_name in contacts:
                print(f"🔍 Found: {search_name} - {contacts[search_name]}")
            else:
                print(f"❌ '{search_name}' not found in contacts.")

        elif choice == "3":
            print("Exiting application. Goodbye!")
            break

        else:
            print("Invalid input. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()