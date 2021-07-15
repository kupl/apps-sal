import sys

num_n = int(sys.stdin.readline())
A = [int(x) for x in sys.stdin.readline()[:-1].split(" ")]
B = [int(x) for x in sys.stdin.readline()[:-1].split(" ")]
B1 = B.copy()

A.sort()
B.sort()

umap = {}

for num in B:
	if num in umap:
		umap[num].append(A.pop())
	else:
		umap[num] = list([A.pop()])

for num in B1:
	print(umap[num].pop(), end=' ')
