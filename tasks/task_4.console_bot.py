
def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args: list, contacts: dict) -> str:
    if len(args) < 2:
        user_input = input("Please provide a name and a new phone number (e.g. 'John 1234567890'): ")
        args = user_input.split()
    
    name, phone = args[0].rstrip(), args[1].rstrip()
    contacts[name] = phone
    return "Contact added."

def change_contact(args: list, contacts: dict) -> str:
    if len(args) < 2:
        user_input = input("Please provide an existing name and a new phone number (e.g. 'John 1234567890'): ")
        args = user_input.split()
    
    name, new_phone = args[0].rstrip(), args[1].rstrip()
    
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return f"No contact found with name: {name}"

def show_phone(args: list, contacts: dict) -> str:
    if len(args) < 1:
        user_input = input("Please provide an existing name (e.g. 'John'): ")
        args = user_input.rstrip()
    name = args[0]
    return contacts.get(name, f"No contact found with name: {name}")

def show_all(contacts: dict) -> str:
    if not contacts:
        return "Empty list."
    return '\n'.join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        
        try:
            if command in ["hi", "hello", "whatsup"]:
                print("How can I help you?")
            elif command in ["new", "add"]:
                print(add_contact(args, contacts))
            elif command in ["change", "update"]:
                print(change_contact(args, contacts))
            elif command in ["phone", "find"]:
                print(show_phone(args, contacts))
            elif command in ["all", "show"]:
                print(show_all(contacts))
            elif command in ["close", "exit", "bye"]:
                print("Good bye!")
                break
            else:
                print("Invalid command.")
        except Exception as e:
            print(f"An error occurred: {e}. Try again.")

if __name__ == "__main__":
    main()
