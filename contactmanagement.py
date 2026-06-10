FILENAME = "contacts.txt"

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    file = open(FILENAME, "a")
    file.write(name + "," + phone + "," + email + "," + address + "\n")
    file.close()

    print("Contact Added Successfully!")

def view_contacts():
    try:
        file = open(FILENAME, "r")
        contacts = file.readlines()
        file.close()

        if len(contacts) == 0:
            print("No Contacts Found!")
        else:
            print("\nContact List:")
            for contact in contacts:
                data = contact.strip().split(",")
                print("Name:", data[0], "| Phone:", data[1])

    except FileNotFoundError:
        print("No Contacts Found!")

def search_contact():
    search = input("Enter Name or Phone: ")

    try:
        file = open(FILENAME, "r")
        contacts = file.readlines()
        file.close()

        found = False

        for contact in contacts:
            data = contact.strip().split(",")

            if search == data[0] or search == data[1]:
                print("\nContact Found:")
                print("Name:", data[0])
                print("Phone:", data[1])
                print("Email:", data[2])
                print("Address:", data[3])
                found = True

        if not found:
            print("Contact Not Found!")

    except FileNotFoundError:
        print("No Contacts Found!")

def update_contact():
    name = input("Enter Name to Update: ")

    try:
        file = open(FILENAME, "r")
        contacts = file.readlines()
        file.close()

        updated = False

        for i in range(len(contacts)):
            data = contacts[i].strip().split(",")

            if data[0] == name:
                phone = input("Enter New Phone: ")
                email = input("Enter New Email: ")
                address = input("Enter New Address: ")

                contacts[i] = name + "," + phone + "," + email + "," + address + "\n"
                updated = True
                break

        if updated:
            file = open(FILENAME, "w")
            file.writelines(contacts)
            file.close()
            print("Contact Updated Successfully!")
        else:
            print("Contact Not Found!")

    except FileNotFoundError:
        print("No Contacts Found!")

def delete_contact():
    name = input("Enter Name to Delete: ")

    try:
        file = open(FILENAME, "r")
        contacts = file.readlines()
        file.close()

        new_contacts = []
        deleted = False

        for contact in contacts:
            data = contact.strip().split(",")

            if data[0] != name:
                new_contacts.append(contact)
            else:
                deleted = True

        if deleted:
            file = open(FILENAME, "w")
            file.writelines(new_contacts)
            file.close()
            print("Contact Deleted Successfully!")
        else:
            print("Contact Not Found!")

    except FileNotFoundError:
        print("No Contacts Found!")

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")