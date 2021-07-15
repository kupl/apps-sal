t=int(input())
for i in range(t):
    K=int(input())
    l=list(range(K+1))
    for x in range(2*K+1):
        print(" "*abs(K-x),end="")
        for y in range(K+1-abs(K-x)):
            print(l[-y-1],end="")
        print()
