
import sys
#sys.stdin=open("data.txt")
input=sys.stdin.readline

n=int(input())

c=list(map(int,input().split()))
ans=0

for i in range(n):
    # match the first person
    f=c.pop(0)
    g=c.index(f)
    c.pop(g)
    ans+=g

print(ans)
