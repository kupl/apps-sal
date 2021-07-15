t=int(input())
for t in range(t):
    n=int(input())
    for i in range(0,n):
        for j in range(0,n):
            if j%2==0:
                print(1,end="")
            else:
                print(0,end="")
        print()
            

