# cook your dish here
for _ in range(int(input())):
    n=int(input())
    print("0")
    for i in range(1,n+1):
        for j in range(i):
            print("*",end="")
        print(i)


