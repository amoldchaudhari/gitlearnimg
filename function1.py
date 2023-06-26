from multiply import multiply
from division import division
from subtraction import subtraction



   
num1= int(input("Enter number 1st digit: "))
num2= int(input("enter number 2nd digit: "))
operator=input("what you want to do operator, ( + - * / % )")
print ("operator")
if (operator == "*"):
        result = multiply(num1, num2)
elif (operator == "/"):
        result = division(num1, num2)
elif (operator == "-"):
        result = subtraction(num1, num2)
print(result)
    