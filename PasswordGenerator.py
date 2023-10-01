import string
import random


def generate_password(length, use_lower, use_upper, use_number, use_special):
    # Define character sets
    lower_chars = list(string.ascii_lowercase)
    upper_chars = list(string.ascii_uppercase)
    number_chars = list(string.digits)
    special_chars = ['$', '%', '^', '&', '*',
                     '(', ')', '_', '+', '=', '-', '!', ';', ':', ',', '.', '[', ']', '{', '}']

    # Initialize the list of allowed character sets and password
    allowed_sets = []
    password = ""

    # Check and add lower case characters
    if use_lower:
        allowed_sets.append(lower_chars)
        password += random.choice(lower_chars)

    # Check and add upper case characters
    if use_upper:
        allowed_sets.append(upper_chars)
        password += random.choice(upper_chars)

    # Check and add numbers
    if use_number:
        allowed_sets.append(number_chars)
        password += random.choice(number_chars)

    # Check and add special characters
    if use_special:
        allowed_sets.append(special_chars)
        password += random.choice(special_chars)

    # Validate that at least one set is allowed
    if not allowed_sets:
        print("At least one character set must be allowed.")
        return None

    # Generate the remaining characters randomly
    for _ in range(length - len(password)):
        selected_set = random.choice(allowed_sets)
        password += random.choice(selected_set)

    # Shuffle the password characters for randomness
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password


print("Password Generator")
password_length = int(input("Enter Password Length: "))
include_lower = input("Include Lowercase (y/n): ").lower() == 'y'
include_upper = input("Include Uppercase (y/n): ").lower() == 'y'
include_number = input("Include Numbers (y/n): ").lower() == 'y'
include_special = input("Include Special Characters (y/n): ").lower() == 'y'

generated_password = generate_password(
    password_length, include_lower, include_upper, include_number, include_special)

if generated_password:
    print("-" * 20, "Password", "-" * 20)
    print(generated_password)
