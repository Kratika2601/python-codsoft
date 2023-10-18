contacts = {}

def add_contact():
    name=input("Enter the name: ")
    phone=input("Enter the phone number: ")
    email=input("Enter the Email: ")
    address=input("Enter the address: ")
    contacts[name] ={"Phone no.":phone,"Email":email,"Address":address}
    print("%s has been added to your contacts!" %name)

def view_contact_list():
    if contacts:
        print("CONTACT BOOK")
        for name,phone in contacts.items():
            print(f"{name}:{phone}")
    else:
        print("Your contact book is empty!")

def search_contact():
    name = input("Enter the name to search: ")
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("%s not found in your contacts." %name)

def delete_contact():
    name = input("Enter the name to delete: ")
    if name in contacts:
        del contacts[name]
        print("%s has been deleted from your contacts!" %name)
    else:
        print("%s not found in your contacts." %name)


while True:
        
    print("OPTIONS:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contact_list()
        input("Press Enter to continue...")
    elif choice == "3":
        search_contact()
        input("Press Enter to continue...")
    elif choice == "4":
        delete_contact()
        input("Press Enter to continue...")
    elif choice == "5":
        break
    else:
        print("Invalid choice.")


   

           
