# cook your dish here
t=int(input())
for _ in range(t):
    a,d,k,n,inc=list(map(int,input().split()))
    if(n%k==0):
        c=n//k
    else:
        c=n//k + 1
    while(c>0):
        s=a+(k-1)*d
        d=d+inc
        a=s+d
        c=c-1
    if(n%k==0):
        print(s)
    else:
        r=n%k
        r1=k-r
        print(s-r1*(d-inc))

