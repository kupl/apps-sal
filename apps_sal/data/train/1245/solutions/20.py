# cook your dish here

for _ in range(int(input())):
    n=int(input())
    c=1
    for i in range(1,n+1):
        for j in range(n):
            print(c,end="")
            c+=2
        print()
