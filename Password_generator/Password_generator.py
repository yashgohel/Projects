import secrets
import string

# Define the password length
length = 8

# Define character set: letters, digits, and punctuation
alphabet = string.ascii_letters + string.digits + string.punctuation

# Generate the password
password = "".join(secrets.choice(alphabet) for _ in range(length))

print(password)
