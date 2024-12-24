a=int(input("Enter a number"))
count=1
for i in range (1,a+1):
    for j in range (1, i+1):
        print(count, end=" ")
        count=count+1
    print()