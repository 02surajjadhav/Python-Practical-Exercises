# VI Exercise 2
# Phonebook Application

phonebook = {}

while True:
    print("\n----- PHONEBOOK MENU -----")
    print("1. Add Contact")
    print("2. Display All Contacts")
    print("3. Exit")

    choice = input("Enter your choice: ").strip()

    # Add Contact
    if choice == "1":
        name = input("Enter name: ").strip()
        number = input("Enter contact number: ").strip()

        # Check if contact already exists
        if name in phonebook:
            print("Contact already exists.")
            print("Existing number:", phonebook[name])
            print("Contact was not overwritten.")
        else:
            phonebook[name] = number
            print("Contact added successfully.")

    # Display complete directory
    elif choice == "2":
        if len(phonebook) == 0:
            print("Phonebook is empty.")
        else:
            print("\n----- PHONEBOOK -----")
            print("{:<20} {:<15}".format("Name", "Contact Number"))
            print("-" * 35)

            for name in phonebook:
                print("{:<20} {:<15}".format(
                    name, phonebook[name]
                ))

    # Exit
    elif choice == "3":
        print("Exiting phonebook. Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
