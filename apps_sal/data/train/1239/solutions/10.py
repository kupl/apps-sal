t=int(input())
for _ in range(t):
    n = int(input())
    for i in range(n+1):
        b = n
        for space in range(n-i):
            print(" ",end="")
        for j in range(i+1):
            print(b,end="")
            b-=1
        print()
    for l in range(n):
        a = n
        for space1 in range(0,l+1):
            print(" ",end="")
        for k in range(n-l):
            print(a,end="")
            a-=1
        
        print()
