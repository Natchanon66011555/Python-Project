import random
import string

class PasswordGenerator:
    def __init__(self):
        self.characters = string.ascii_letters + string.digits + "!@#$%"
        self.min_password_length = 8
        self.max_password_length = 15

    def generate_password(self):
        length = random.randint(self.min_password_length, self.max_password_length)
        password = []
        for _ in range(length):
            password.append(random.choice(self.characters))
        return ''.join(password)

class UsernameGenerator:
    def __init__(self):
        self.prefixes = ["user", "admin", "guest"]
        self.suffixes = ["123", "456", "789"]

    def generate_username(self):
        prefix = random.choice(self.prefixes)
        suffix = random.choice(self.suffixes)
        return f"{prefix}_{suffix}"

class PasswordManager:
    def __init__(self):
        self.generated_passwords = set()

    def generate_unique_password(self, generator, max_attempts=10):
        attempts = 0
        while attempts < max_attempts:
            password = generator.generate_password()
            if password not in self.generated_passwords:
                self.generated_passwords.add(password)
                return password
            attempts += 1
        return "Could not generate a unique password"

def write_username_to_file(username, filename="usernames.txt"):
    with open(filename, "a") as file:
        file.write(username + "\n")

def read_usernames_from_file(filename="usernames.txt"):
    try:
        with open(filename, "r") as file:
            return set(file.read().splitlines())
    except FileNotFoundError:
        return set()

# Main program loop
while True:
    username_generator = UsernameGenerator()
    password_generator = PasswordGenerator()
    manager = PasswordManager()

    user_entered_username = input("Enter your own username: ")
    generated_username = user_entered_username.strip()

    existing_usernames = read_usernames_from_file()

    while generated_username in existing_usernames:
        print("Username already exists. Please enter a new one.")
        user_entered_username = input("Enter your own username: ")
        generated_username = user_entered_username.strip()

    create_own_password = input("Would you like to create your own password? (yes/no): ")

    if create_own_password.lower() == "yes":
        user_password = input("Enter your password: ")
    else:
        user_password = manager.generate_unique_password(password_generator)

    print("Generated Password:", user_password)

    user_input = input("Confirm and store this set? (yes/no): ")
    if user_input.lower() == "yes":
        write_username_to_file(generated_username)
        print("Username and password confirmed and stored. Exiting...")
        break
    else:
        print("Confirmation failed. Please generate a new set.")

