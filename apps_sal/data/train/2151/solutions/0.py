
import sys
#sys.stdin=open("data.txt")
input=sys.stdin.readline

n,s=list(map(int,input().split()))

a=list(map(int,input().split()))
a.sort()
med=a[n//2]

ans=0
if med>s:
    for i in range(n//2+1):
        if a[i]>s:
            ans+=a[i]-s
elif med<s:
    for i in range(n//2,n):
        if s>a[i]:
            ans+=s-a[i]
print(ans)


