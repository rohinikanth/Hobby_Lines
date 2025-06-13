#For loop
print("Multiplication Table of 12:")
for i in range(1, 11):
    print(f"12 x {i} = {12 * i}")
  
'''
Sample output:
Multiplication Table of 12:
12 x 1 = 12
12 x 2 = 24
12 x 3 = 36
12 x 4 = 48
12 x 5 = 60
12 x 6 = 72
12 x 7 = 84
12 x 8 = 96
12 x 9 = 108
12 x 10 = 120
'''

#while loop
num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10         
    reverse = reverse * 10 + digit 
    num = num // 10           
print("Reversed number is:", reverse)

'''
Sample output:
Enter a number: 3467
Reversed number is: 7643
'''

#if-else
from sympy import isprime

for i in range(1, 20):
    output = ""

    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    if output == "" and isprime(i):
        output = "Prime"
    elif output == "":
        output = str(i)

    print(output)

'''
Sample output
1
Prime
Fizz
4
Buzz
Fizz
Prime
8
Fizz
Buzz
Prime
Fizz
Prime
14
FizzBuzz
16
Prime
Fizz
Prime
'''

