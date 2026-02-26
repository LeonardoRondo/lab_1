#Autor: Alexander Duran
#1. Addittion of n numbers
print("Addition of n numbers.")
n = int(input("Quantity of numbers to add: "))
total_sum = 0
for i in range(n):
    new_number = float(input(f"Enter the number to add number {i+1}: "))
    total_sum += new_number
print(f"La suma total es: {total_sum}\n")

#2.Gets the inverted numbers
print("Inverted numbers")
inv_num = input("Enter the number to invert: ")
num_inv = inv_num[::-1] 
print(f"The inverted number is: {num_inv}\n")

# 3.Asks name, age and profession and returns a message
print("Custom message")
name = input("Enter your name: ")
age = input("Enter your age: ")
prof = input("Enter your profession: ")
print(f"{name}, congrats at being hired as a {prof} at yours {age}th Birthday!")

# 4.Asks x numbers and returns only unique values
print("Only Unique values")
num_input = input("Enter spaced numbers (ex. 1 2 2 3 4 4 5): ")
num_list = num_input.split()
unique_list = list(set(num_list))
print(f"The list of unique values is: {unique_list}")
