from collections import defaultdict
def DFS(d,visited,x):

	stack = [x]
	ans = []

	while len(stack):

		temp = stack.pop()
		visited[temp] = 1
		ans.append(temp+1)
		for i in d[temp]:

			if visited[i] == 0:
				stack.append(i)
				visited[temp] = 1

	return ans

n = int(input())
l = list(map(int,input().split()))
act_pos = {l[i]:i for i in range(n)}
pos = []
t = sorted(l)
pos = {t[i]:i for i in range(n)}

d = defaultdict(list)

for i in l:

	d[act_pos[i]].append(pos[i])


visited = [0 for i in range(n)]
ans = []
for i in range(n):

	if visited[i] == 0:

		k = list(DFS(d,visited,i))

		t1 = k[::-1]
		t1.append(len(k))

		ans.append(t1[::-1])
print(len(ans))
for i in ans:
	print(*i)

