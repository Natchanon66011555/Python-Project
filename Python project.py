import random

class PasswordGenerator:
    def __init__(self):
        self.characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.password_length = 15

    def generate_password(self, length):
        password = []
        for _ in range(length):
            password.append(random.choice(self.characters))
        return ''.join(password)
    
class PasswordManager:
    def __init__(self):
        self.generated_passwords = set()

    def generate_unique_password(self, generator, max_attempts=10):
        attempts = 0
        while attempts < max_attempts:
            password = generator.generate_password(random.randint(1, generator.password_length))
            if password not in self.generated_passwords:
                self.generated_passwords.add(password)
                return password
            attempts += 1
        return "Could not generate a unique password"