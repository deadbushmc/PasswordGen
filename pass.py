import random
import string
import time

t = 1
def intro():
    print("Welcome To Password Generator")
    time.sleep(t)
    print("Made By DeadBush")
    time.sleep(t)
    gen()

def gen():
    print("Following Numbers Are ASsigned To The Following Stuff")
    print("1 for Letters Only")
    print("2 for Digits")
    print("3 for Mix")
    take_input = eval(input("Enter Your Values"))
    length=int(input("Enter the password legth: "))
    if take_input == 1:
        print("Generating Your Password Please Wait")
        time.sleep(3)
        password = ''.join(random.choices(string.ascii_letters, k = length))
        print(f"Your password is: {password}")
        time.sleep(t)
        cb=input("Do you want to continue? [y/n]: ")
        cont(cb)
    elif take_input == 2:
        print("Generating Your Password Please Wait")
        time.sleep(3)
        password = ''.join(random.choices(string.digits, k = length))
        print(f"Your password is: {password}")
        time.sleep(t)
        cb=input("Do you want to continue? [y/n]")
        cont(cb)
    elif take_input == 3:
        print("Generating Your Password")
        time.sleep(3)
        password = ''.join(random.choices(string.ascii_letters + string.punctuation + string.digits, k = length))
        print(f"Your password is: {password}")
        time.sleep(t)
        cb=input("Do you want to continue? [y/n]")
        cont(cb)

def cont(cb):
    if cb.lower() == "y":
        intro()
    elif cb.lower() == "n":
        outro()
    else:
        print(f"{cb} is not a valid option")
        print("Abort")

def outro():
    print("Thank you for using password gen by DeadBush!")

intro()
