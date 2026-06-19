import random
import string

print("=" * 50)
print("      RANDOM PASSWORD GENERATOR")
print("=" * 50)

while True:
    try:
        length = int(input("Enter password length (minimum 6): "))

        if length < 6:
            print("Password length must be at least 6.")
            continue

        break

    except ValueError:
        print("Please enter a valid number.")

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
special = "@#$%&*!"

all_characters = lowercase + uppercase + digits + special

password = [
    random.choice(lowercase),
    random.choice(uppercase),
    random.choice(digits),
    random.choice(special)
]

for i in range(length - 4):
    password.append(random.choice(all_characters))

random.shuffle(password)

final_password = "".join(password)

print("\nGenerated Secure Password:")
print(final_password)

print("\nPassword Strength: STRONG")
print("=" * 50)
