# cook your dish here
t=int(input())
for i in range(t):
    a,d,k,n,inc=map(int,input().split())
    for i in range(1,n):
        if i%k==0:
            d=d+inc
            a=a+d
        else:
            a=a+d
    print(a) 
