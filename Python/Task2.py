#Sort a List of Tuples by the Second Item Using Lambda Function.
students = [("Alice", 88), ("Bob", 72), ("Charlie", 95), ("David", 85)]
sorted_students = sorted(students, key=lambda x: x[1])
print("Sorted List by Score:")
print(sorted_students)

'''
Sample output:
Sorted List by Score:
[('Bob', 72), ('David', 85), ('Alice', 88), ('Charlie', 95)]
'''

#Write a Python program that takes two numbers as input and performs all basic arithmetic operations (addition, subtraction, multiplication, division, and modulus). Each operation must be implemented using a separate function.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def modulus(x, y):
    if y != 0:
        return x % y
    else:
        return "Error! Modulus by zero."

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"{num1} + {num2} = {add(num1, num2)}")
print(f"{num1} - {num2} = {subtract(num1, num2)}")
print(f"{num1} * {num2} = {multiply(num1, num2)}")
print(f"{num1} / {num2} = {division(num1, num2)}")
print(f"{num1} % {num2} = {modulus(num1, num2)}")

'''
Sample output:
Enter first number: 50
Enter second number: 5
50 + 5 = 55
50 - 5 = 45
50 * 5 = 250
50 / 5 = 10
50 % 5 = 0

Enter first number: 10
Enter second number: 3
10 + 3 = 13
10 - 3 = 7
10 * 3 = 30
10 / 3 = 3.3333333333333335
10 % 3 = 1
'''
