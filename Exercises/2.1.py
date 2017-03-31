num1 = int(raw_input("Enter first number "))
num2 = int(raw_input("Enter second number "))
if (num1>num2):
    temp = num1
    num1 = num2
    num2 = temp

for i in range(num1,num2+1):
    print i
