count=0
n=int(input())
for __ in range(n):
    a,b=map(int,input().split())
    count+=b-a
print((count+n)%1000000007)
