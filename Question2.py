def input_length_validator():
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")

    if len(first_name) < 2:
        print("Error: First name must be at least 2 characters long.")
    elif len(last_name) < 2:
        print("Error: Last name must be at least 2 characters long.")
    else:
        print("Thank you! Your names are valid.")

if __name__ == "__main__":
    input_length_validator()
