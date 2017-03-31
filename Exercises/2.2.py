num = int(raw_input("Enter number "))

for i in range(num,0,-1):
    print ""
    for j in range(0,num-i+1):
        print "*",
