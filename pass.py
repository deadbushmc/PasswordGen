import random
import string

length=int(input("Enter the password legth"))

password = ''.join(random.choices(string.ascii_letters + string.punctuation + string.digits, k = length))

print(f"Your password is: {password}")