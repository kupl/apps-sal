from sys import stdin
input=lambda : stdin.readline().strip()
from math import ceil,sqrt,factorial,gcd
from collections import deque
n=int(input())
l=list(map(int,input().split()))
s=list(map(int,input().split()))
graph={i:set() for i in range(1,n+1)}
for i in range(n-1):
	graph[l[i]].add(i+2)
level=[[] for i in range(n+2)]
stack=[[1,1]]
flag=1
while stack:
	x,y=stack.pop()
	level[y].append(x)
	for i in graph[x]:
		stack.append([i,y+1])
# print(level)
ans=[0 for i in range(n+2)]
ans[1]=s[0]
for i in range(1,n+1):
	if i%2==0:
		for j in level[i]:
			papa=s[l[j-2]-1]
			if len(graph[j])==0:
				s[j-1]=papa
				ans[j]=0
			else:
				mi=float("infinity")
				for k in graph[j]:
					mi=min(mi,s[k-1])
					if s[k-1]<papa:
						flag=0
						break
				ans[j]=mi-papa
				s[j-1]=papa+ans[j]
	else:
		if i>1:
			for j in level[i]:
				papa=s[l[j-2]-1]
				# print(papa)
				ans[j]=s[j-1]-papa
# print(ans)
if flag==0:
	print(-1)
else:
	print(sum(ans))

