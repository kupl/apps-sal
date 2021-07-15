n=int(input())
s=0
for z in range(n):
    b,d=list(map(int,input().split()))
    if b>=0 and d>=0:
        s=s+(d-b+1)
        s%=10**9+7
    elif b<0 and d>=0:
        s+=(d+abs(b)+1)
        s%=10**9+7
    else:
        s+=(abs(b)-abs(d)+1)
        s%=10**9+7
print(s%(1000000000+7))



