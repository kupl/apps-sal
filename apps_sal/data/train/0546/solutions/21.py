t=int(input())
while(t!=0):
    k=0
    n=int(input())
    if n&n-1==0:
        print(0)
    else:
        while(n!=0):
             n=n&n-1
             k+=1
        print(k-1)
    t-=1



