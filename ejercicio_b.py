from classes.Contact import Contact

contacts = []

def main():
    # We'll add closures here for adding, updating, printing and removing
    def add(contact: Contact, i: int) -> None:
        """
        Adds a contact to the contact list
        """
        contacts.insert(i if i else len(contacts), contact)

    def remove(i: int) -> None:
        """
        Removes a contact from the contact list, based in the index
        """
        del contacts[i]

    def update(contact: Contact, i: int):
        """
        Receives a contact object and updates the index
        """
        contacts[i].name = (
            contact.name
            if contact.name != "" else contacts[i].name
        )
        contacts[i].number = (
            contact.number
            if contact.number != "" else contacts[i].number
        )

    def display():
        """
        Prints all of the contacts
        """
        if len(contacts) == 0:
            print("No contacts!\n")
            return

        for i, o in enumerate(contacts):
            print(f"[{i}]: {str(o)}")
        print("\n")

    print("Manage contacts:")
    print("Options: A (add), R (remove), U (update), E (exit)")
    print("To perform an operation, prefix the contact index\nusing the option (for example, A3 to add a contact to the 3rd position)\n")
    while 1:
        display()

        operation = input("Perform an operation: ")
        if len(operation) < 1:
            print("Invalid operation!\n")
            continue

        option = operation[0]
        index = int(operation[1:]) if len(operation) > 1 else None

        match option:
            case "A":
                add(
                    Contact(
                        input("Contact name: "),
                        input("Contact number: ")
                    ),
                    index
                )
            case "R":
                if index is None:
                    print("Index is required!\n")
                    continue
                remove(index)
            case "U":
                if index is None:
                    print("Index is required!\n")
                    continue
                update(
                    Contact(
                        input("New name (blank to not change): "),
                        input("New number (blank to not change): ")
                    ),
                    index
                )
            case "E":
                exit(0)

if __name__ == "__main__":
    main()
