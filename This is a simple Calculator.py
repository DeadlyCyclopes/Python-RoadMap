print("This is a simple Calculator")

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

op = input("Enter an operand among +, -, /, *: ")
if op == '+':
     print('num1 + num2 =',num1+num2)
elif op == '-':
     print('num1 - num2 =',num1-num2)
elif op == '/':
     print('num1 / num2 =', num1/num2)
elif op == '*':
     print('num1 * num2 =', num1*num2 )
else :
    print('error')