# Contact Book

contacts = {}

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contacts[name] = phone
        print("Contact added successfully! ✅")

    elif choice == "2":
        print("\n--- Contacts ---")

        if len(contacts) == 0:
            print("No contacts available.")

        else:
            for name, phone in contacts.items():
                print(name, ":", phone)

    elif choice == "3":
        name = input("Enter name to search: ")

        if name in contacts:
            print("Phone number:", contacts[name])
        else:
            print("Contact not found. ❌")

    elif choice == "4":
        print("Thank you! 👋")
        break

    else:
        print("Invalid choice. Try again.")