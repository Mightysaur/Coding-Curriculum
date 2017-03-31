listOfNum = []

for i in range(0,10):
    num = int(raw_input("Enter number "))
    listOfNum.append(num)

even = []
odd = []

for i in range(0,10):
    if(listOfNum[i]%2 == 0):
        even.append(listOfNum[i])
    else:
        odd.append(listOfNum[i])

print even
print odd
