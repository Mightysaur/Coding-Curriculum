loop = True
tot = 0
while loop:
    item = raw_input("Enter number ")
    if(item == "stop"):
        break
    else:
        tot = tot + float(item)

print tot
