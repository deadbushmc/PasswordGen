import random
import string
import time

t = 1
def intro():
    print("Welcome to password gen")
    time.sleep(t)
    print("By DeadBush")
    time.sleep(t)
    gen()

def gen():
    length=int(input("Enter the password legth: "))
    print("Generating Your Password Please Wait")
    time.sleep(3)
    password = ''.join(random.choices(string.ascii_letters + string.punctuation + string.digits, k = length))
    print(f"Your password is: {password}")
    time.sleep(t)
    cb=input("Do you want to continue? [y/n]: ")
    cont(cb)

def cont(cb):
    if cb.lower() == "y":
        intro()
    elif cb.lower() == "n":
        outro()
    else:
        print(f"{cb} is not a valid option")

def outro():
    print("Thank you for using password gen by DeadBush!")

intro()
