import random
import string

# ask for password length and write answer to variable
length=int(input("Enter the password length: "))

# skip a line
print("")

# generate a password (somehow)
password = ''.join(random.choices(string.ascii_letters + string.punctuation + string.digits, k = length))

# output the password :)
print(f"Your password is: {password}")
