def parse_input(user_input):
    """Parses the user input string into a command and its arguments."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()  # Normalize the command to lower case
    return cmd, args

def add_contact(args, contacts):
    """Adds a new contact or updates an existing one in the contacts dictionary."""
    if len(args) != 2:
        return "Invalid input. Use: add name phone"
    name, phone = args
    contacts[name] = phone  # Add or update the contact
    return "Contact added."

def change_contact(args, contacts):
    """Changes the phone number for an existing contact."""
    if len(args) != 2:
        return "Invalid input. Use: change name phone"
    name, phone = args
    if name in contacts:
        contacts[name] = phone  # Update the contact's phone number
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(args, contacts):
    """Shows the phone number for the specified contact."""
    if len(args) != 1:
        return "Invalid input. Use: phone name"
    name = args[0]
    if name in contacts:
        return contacts[name]  # Return the phone number
    else:
        return "Contact not found."

def show_all(contacts):
    """Shows all contacts and their phone numbers."""
    if not contacts:
        return "No contacts found."
    return '\n'.join(f"{name}: {phone}" for name, phone in contacts.items())  # Format all contacts for display

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
