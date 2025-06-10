'''
# Introducing print parameters sep , end , flush

1. sep (separator):
   - Default: ' ' (space)
   - Controls what appears between printed values
   - Examples: sep=', ', sep='|', sep=''

2. end (ending):
   - Default: '\\n' (newline)
   - Controls what appears after all values
   - Examples: end='', end='...', end='\\r'

3. flush (force output):
   - Default: False
   - When True, forces immediate output
   - Useful for real-time updates and logging

'''
print("Apple", "Banana", "Cherry")
print("Apple", "Banana", "Cherry", sep=" | ")
print("Apple", "Banana", "Cherry", sep=" , ")

#Sample Output
'''
Apple Banana Cherry
Apple | Banana | Cherry
Apple , Banana , Cherry
'''

print("Completed!")
print("Completed!",end = '...')
print("Completed!",end =' ')
print("Completed!",end = '\\r')

#Sample Output
'''
Completed!
Completed!...Completed! Completed!\r
'''

#print("Completed!",end = '\r')

#Using Operators
# Simple calculator using operators
def simple_calculator():
    print("\nSimple Calculator")
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ") or "+"
    
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0 :
            result = num1 / num2 
        else :
            print("Error: Division by zero!")
    else:
        result = "Invalid operator"
    
    print(f"Result: {num1} {operator} {num2} = {result}")

simple_calculator()

'''
Sample Output

1.Simple Calculator
Enter first number: 10 
Enter second number: 4
Enter operator (+, -, *, /): =
Result: 10.0 = 4.0 = Invalid operator

2.Simple Calculator
Enter first number: 4
Enter second number: -10
Enter operator (+, -, *, /): +
Result: 4.0 + -10.0 = -6.0

3.Simple Calculator
Enter first number: 9
Enter second number: 4
Enter operator (+, -, *, /): *
Result: 9.0 * 4.0 = 36.0

4.Simple Calculator
Enter first number: 78
Enter second number: 45
Enter operator (+, -, *, /): /
Result: 78.0 / 45.0 = 1.7333333333333334

5.Simple Calculator
Enter first number: 655
Enter second number: 689
Enter operator (+, -, *, /): -
Result: 655.0 - 689.0 = -34.0
'''
