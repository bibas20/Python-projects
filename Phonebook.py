# Phonebook Application

# Step 2: Initialize the Phonebook
phonebook = {}

# Step 3: Display Menu in a Loop
def display_menu():
    print("\nPhonebook Menu:")
    print("1. Add New Contact")
    print("2. Search for Contact")
    print("3. Delete Contact")
    print("4. List All Contacts")
    print("5. Exit")

# Step 4: Implement CRUD Operations
while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter contact name: ").strip()
        if name in phonebook:
            print(f"{name} already exists with number {phonebook[name]}")
        else:
            number = input("Enter phone number: ").strip()
            phonebook[name] = number
            print(f"{name} has been added to the phonebook.")

    elif choice == "2":
        name = input("Enter name to search: ").strip()
        if name in phonebook:
            print(f"{name}'s number is {phonebook[name]}")
        else:
            print(f"{name} was not found in the phonebook.")

    elif choice == "3":
        name = input("Enter name to delete: ").strip()
        if name in phonebook:
            del phonebook[name]
            print(f"{name} has been deleted.")
        else:
            print(f"{name} was not found in the phonebook.")

    elif choice == "4":
        if not phonebook:
            print("Phonebook is empty.")
        else:
            print("\nAll Contacts:")
            for name, number in phonebook.items():
                print(f"{name}: {number}")

    elif choice == "5":
        print("Exiting Phonebook Application. Goodbye!")
        break

    else:1
    print("Invalid choice! Please enter a number from 1 to 5.")
