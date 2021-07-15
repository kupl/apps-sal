t=int(input())
for i in range(0,t):
    n=int(input())
    for j in range(0,n):
        p=1
        for k in range(0,2*n):
            if k%2==0:
                print(p,end="")
                p=p+1
            else:
                print(j+1,end="")
        print(" ")
