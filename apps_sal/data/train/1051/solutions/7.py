from sys import*
input=stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    for i in range(n+1):
        d=i
        for j in range(i+1):
            if d>0:
                print("*",end="")
                d-=1
            else:
                print(j,end="")
        print()

