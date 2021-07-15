# from debug import debug
import sys; input = sys.stdin.readline
n = int(input())
lis = [0, *list(map(int , input().split()))]
v = [0]*(n+1)
cycles = set()
roots = set()
for i in range(1, n+1):
	if v[i] == 0:
		node = i
		while v[node] == 0:
			v[node] = 1
			node = lis[node]
		if v[node] == 2: continue
		start = node
		ignore = 0
		l = 1
		while lis[node] != start:
			if v[node] == 2: ignore = 1; break
			v[node] = 2
			node = lis[node]
			l+=1
		if ignore: continue
		v[node] = 2
		if l == 1: roots.add(node)
		else: cycles.add(node)
ans = 0
if roots:
	base = roots.pop()
	for i in roots: lis[i] = base; ans+=1
	for i in cycles: lis[i] = base; ans+=1
elif cycles:
	base = cycles.pop()
	cycles.add(base)
	for i in roots: lis[i] = base; ans+=1
	for i in cycles: lis[i] = base; ans+=1
print(ans)
print(*lis[1:])

