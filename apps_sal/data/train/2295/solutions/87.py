import sys
n=int(input())

is_same=True
m=10**10
ans=0
for _ in range(n):
    a,b=map(int,input().split())
    if a!=b: is_same=False
    if a>b: m=min(m,b)
    ans+=a

ans-=m
print(ans if not is_same else 0)
