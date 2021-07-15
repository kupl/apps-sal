# cook your dish here
t = int(input())
for i in range(0,t):
    a=input().split()
    b=list(map(int,a))
    n=int(b[2]/b[0])
    if((b[0])*n+b[1]<=b[2]):
        print((b[0])*n+b[1])
    else:
        print((b[0])*(n-1)+b[1])
