m=10**9+7
T=int(input())
while(T>0):
    num=list(map(int,input()))
    n=0
    for i in range(len(num)):
        n=(n*10)%m
        n=(n+num[i])%m
    rs=n
    y=10**(len(num))%m
    for i in range(len(num)-1):
        n=(n*10-(y-1)*num[i])%m
        rs=(rs*(y)+n)%m
    print(rs)
    T-=1
