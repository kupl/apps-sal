# cook your dish here
primes=set([2,3,5,7,11,13,17])

edge=[(0,3),(0,1),(1,2),(1,4),(2,5),(3,4),(3,6),(4,5),(4,7),(5,8),(6,7),(7,8)]
edge=[(0,3),(2,5),(3,4),(4,5),(3,6),(4,7),(5,8),(6,7),(7,8),(0,1),(1,2),(1,4)]
x=list(range(1,10))
from collections import deque
queue=deque([x])
resource={tuple(x):0}
while queue:
	cur=queue.popleft()
	# print(cur)
	for ele in edge:
		if cur[ele[0]]+cur[ele[1]] in primes:
			curr=cur[0:]
			curr[ele[0]],curr[ele[1]]=curr[ele[1]],curr[ele[0]]
			
			ref=tuple(curr)
	
			if ref not in resource:
				resource[tuple(ref)]=resource[tuple(cur)]+1
				queue.append(curr)
			
for _ in range(int(input())):
	lis=[]
	line=input()
	for i in range(3):
		line=input()	
		
		for j in line.split():
			lis.append(int(j))
	lis=tuple(lis)
	# print(lis)
	if lis in resource: print(resource[lis])
	else:print(-1)
			
