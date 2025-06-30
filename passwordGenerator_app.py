import random
import string

def generate_password(length=12):
    # Define the character set: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
password = generate_password(12)
print("Generated Password:", password)