class Contact:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number

class Phonebook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        self.contacts[contact.name] = contact

    def get_contact(self, name):
        return self.contacts.get(name)

def main():
    phonebook = Phonebook()
    
    while True:
        print("\nPhonebook Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter Name: ")
            address = input("Enter Address: ")
            phone_number = input("Enter Phone Number: ")
            contact = Contact(name, address, phone_number)
            phonebook.add_contact(contact)
            print("Contact added successfully!")
        elif choice == '2':
            name = input("Enter Name to search: ")
            contact = phonebook.get_contact(name)
            if contact:
                print("Name:", contact.name)
                print("Address:", contact.address)
                print("Phone Number:", contact.phone_number)
            else:
                print("Contact not found!")
        elif choice == '3':
            print("Exiting Phonebook. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
