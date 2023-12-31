import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

password_length = int(input("Enter desired password length: "))
print("Generated password:", generate_password(password_length))
