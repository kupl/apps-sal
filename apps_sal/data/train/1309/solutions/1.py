for i in range(int(input())):
    p=int(input())
    for i in range(p):
        for k in range(i):
            print("*", end="")
        for j in range(i,p):
            print(p-j, end="")
        print()
            
