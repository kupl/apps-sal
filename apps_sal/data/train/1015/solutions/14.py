t=int(input())
for i in range(0,t):
    n=int(input())
    p=2
    for j in range(0,n):
        for k in range(0,n):
            print(p,end="")
            p=p+2
        print(" ")
