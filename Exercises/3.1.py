listOfNum = []

for i in range(0,10):
    num = int(raw_input("Enter number "))
    listOfNum.append(num)

highest = listOfNum[0]
for i in range(1,10):
    if(highest < listOfNum[i]):
        highest = listOfNum[i]

print highest
