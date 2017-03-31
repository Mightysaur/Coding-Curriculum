shoppingListName = []
shoppingListPrice = []

loop = True
tot = 0
while loop:
    item = raw_input("Enter item name ")
    if(item == "stop"):
        break
    else:
        shoppingListName.append(item)
        price = raw_input("Enter item price ")
        shoppingListPrice.append(price)
        tot = tot + float(price)

for i in range(0,len(shoppingListName)):
    print shoppingListName[i],
    print " ",
    print shoppingListPrice[i]

print tot
