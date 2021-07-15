import sys
input=sys.stdin.readline
n=int(input())
B=[]
ans=0
for i in range(n):
	a,b=map(int,input().split())
	ans+=a
	if a>b:
		B.append(b)
if len(B)==0:
	print(0)
else:
	print(ans-min(B))
