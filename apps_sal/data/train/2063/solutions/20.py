p = [i for i in range(110)]
rank = [0 for i in range(110)]

def findSet(i):
	nonlocal p
	if(p[i]==i):
		return i
	p[i] = findSet(p[i])
	return p[i]

def isSameSet(i,j):
	return findSet(i)==findSet(j)

def unionSet(i,j):
	nonlocal p,rank
	if(isSameSet(i,j)):
		return
	x = findSet(i)
	y = findSet(j)
	if(rank[x]>rank[y]):
		p[y] = x
	else:
		p[x] = y
		if(rank[x]==rank[y]):
			rank[y]+=1

n,m = tuple(int(i) for i in input().split())
langs = [set() for i in range(n)]

allzero = True
for i in range(n):
	A = list(int(i) for i in input().split())
	if(A[0]!=0):
		allzero = False
	for j in range(len(A)):
		if(j>0):
			langs[i].add(A[j])
if not allzero:
	for i in range(n):
		for j in range(i+1,n):
			if(len(langs[i] & langs[j])>=1):
				unionSet(i,j)

	roots = set()
	for i in range(n):
		roots.add(findSet(i))

	print(len(roots)-1)
else:
	print(n)
