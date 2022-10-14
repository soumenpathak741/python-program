# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result
print("enter 1st number: ")
num1=int(input())
print("enter 2nd number: ")
num2=int(input())
print('what you want?'+'+,-,/,*,%')
num3=input()
if num1==45 and num2==3 and num3=='*':
    print(555)
elif num1==56 and num1==9 and num3=='+':
    print(77)
elif num1 == 56 and num1 == 9 and num3 == '/':
    print(4)
elif num3=='+':
    Add=num1+num2
    print(Add)
elif num3=='-':
    Sub=num1-num2
    print(Sub)
elif num3=='/':
     Div=num1/num2
     print(Div)
elif num3=='*':
    Mul=num1*num2
    print(Mul)
elif num3=='%':
     Mod=num1%num2
     print(Mod)
else:
     print("Error! please check your number")

