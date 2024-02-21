import random
import string

def get_user_input():
    while True:
        try:
            password_length = int(input("Enter password length (min 8): "))
            if password_length < 8:
                print("Password length must be at least 8.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        character_types = input("Choose character types (l)letters, (n)numbers, (s)symbols: ")
        if not all(char in "lns" for char in character_types):
            print("Invalid input. Please enter l, n, or s.")
            continue

        break

    character_sets = {
        "l": string.ascii_letters,
        "n": string.digits,
        "s": string.punctuation
    }

    password_characters = "".join(character_sets[char_type] for char_type in character_types)

    password = generate_password(password_length, password_characters)
    print("Generated password:", password)


def generate_password(length, characters):
    return "".join(random.choice(characters) for _ in range(length))


if __name__ == "__main__":
    get_user_input()
