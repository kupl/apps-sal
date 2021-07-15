
tree_size = int(input())

parents = [int(x)-1 for x in input().split(' ')]


num_changes = 0

root = tree_size
for node, parent in enumerate(parents):
	if parent == node:
		root = node
		break

visited = set()
finished = set()

visited.add(root)
finished.add(root)

stack = []
fringe = []

for node in range(len(parents)):
	if node not in visited:
		fringe.append(node)
		while fringe:
			cur = fringe.pop()
			visited.add(cur)
			stack.append(cur)

			if parents[cur] not in finished:
				if parents[cur] in visited:
					parents[cur] = root
					num_changes += 1
				else:
					fringe.append(parents[cur])

		while stack:
			finished.add(stack.pop())



if root == tree_size:
	new_root = None
	for node, parent in enumerate(parents):
		if parent == root:
			if new_root is None:
				new_root = node
			parents[node] = new_root

for i in range(len(parents)):
	parents[i] += 1


print(num_changes)
print(*parents)
