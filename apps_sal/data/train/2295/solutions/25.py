N=int(input())
s=0
minus=10**18
flag=True
for i in range(N):
    a,b=map(int,input().split())
    if a>b:
        minus=min(minus,b)
        flag=False
    elif b>a:
        flag=False
    s+=a
if flag:
    print(0)
else:
    print(s-minus)
