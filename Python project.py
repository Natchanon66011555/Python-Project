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
        password.append(random.choice(string.digits))
        for _ in range(length - 1):
            password.append(random.choice(self.characters))
        random.shuffle(password)
        return ''.join(password)

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

# Main program loop
while True:
    generator = PasswordGenerator()
    manager = PasswordManager()

    generated_password = manager.generate_unique_password(generator)
    print("Generated Password:", generated_password)

    user_input = input("Generate another password? (yes/no): ")
    if user_input.lower() != "yes":
        confirm_input = input("Confirm your password (type the generated password): ")
        if confirm_input == generated_password:
            print("Password confirmed. Exiting...")
            break
        else:
            print("Password mismatch. Please generate a new password.")