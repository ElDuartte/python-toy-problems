import secrets  # secrets is a module of Python that provides functions for generating cryptographically strong random numbers.
import string  # string module is a built-in module in Python that provides a collection of string constants and helper functions for working with strings.


def generate(length, use_symbols, use_numbers, use_lowercase, use_uppercase):
    # Empty string to store the characters based on user preferences
    characters = ""

    # Check for the user preferences
    if use_symbols:
        characters += string.punctuation
    if use_numbers:
        characters += string.digits
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase

    # Check if at least one character set is selected
    if not characters.strip():
        print("Error: Select at least one character type")
        return None

    # Generate a password by randomly selecting characters from the combined set
    password = "".join(secrets.choice(characters) for _ in range(length))
    return password


def get_user_input():
    while True:
        try:
            # Get user input for password length
            length_input = input("Enter the password length: ")

            # Check if the length input is empty
            if not length_input:
                raise ValueError("Password length cannot be empty.")

            # Convert the length input to an integer
            length = int(length_input)

            # Check if the length is a positive integer
            if length <= 0:
                raise ValueError("Password length must be a positive integer.")

            # Get user preferences for other parameters
            use_symbols = input("Include symbols? (y/n): ").lower() == "y"
            use_numbers = input("Include numbers? (y/n): ").lower() == "y"
            use_lowercase = (
                input("Include lowercase? (y/n): ").lower() == "y"
            )
            use_uppercase = (
                input("Include uppercase? (y/n): ").lower() == "y"
            )

            # Check if all questions are answered
            if not (use_symbols or use_numbers or use_lowercase or use_uppercase):
                raise ValueError("Select at least one character type")

            # Return the gathered input
            return length, use_symbols, use_numbers, use_lowercase, use_uppercase

        except ValueError as e:
            print(f"Error: {e}")


def main():
    # Get user input
    length, use_symbols, use_numbers, use_lowercase, use_uppercase = get_user_input()

    # Generate a password
    password = generate(length, use_symbols, use_numbers, use_lowercase, use_uppercase)

    # Print the password
    if password:
        print("Password:", password)


# The name convention is wot only execute this function
if __name__ == "__main__":
    main()
