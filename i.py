a=int(input("Enter a number of rows"))
for i in range(1, a+1):
    for j in range(1, a-i+2):
        print("->", end="")
    print()