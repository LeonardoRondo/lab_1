def adding():
    n = int(input("Amount of numbers to add: "))
    sum = 0
    for i in range(n):
        suma += int(input(f"Enter number: "))
    print(f"Total: {suma}\n")

def invert():
    num = int(input("Input a number: "))
    print(f"Inverted number: {num[::-1]}\n")

def msg():
    name = input("Name: ")
    age = input("Age: ")
    prof = input("Profession: ")
    print(f"{name}, at {age} you are great at {prof}")

def unic():
    x = int(input("Amount of number to enter: "))
    l = []
    for i in range(x):
        l.append(input(f"input a number: "))
    unicnum = list(set(l))
    print(f"Unic values: {unicnum}\n")

adding()
invert()
msg()
unic()
