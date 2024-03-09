def process_user_contacts(user_input):
    user_contacts = {}
    tokens = user_input.split()
    for i in range(0, len(tokens), 2):
        name = tokens[i]
        phone_number = tokens[i + 1]
        user_contacts[name] = phone_number

    contact_name = input("Enter the contact name: ")
    print(user_contacts[contact_name])

if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")

    # Call the function to process user contacts
    process_user_contacts(user_input)
