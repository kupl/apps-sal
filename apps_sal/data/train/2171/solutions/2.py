import sys
def read(t=int): return list(map(t, sys.stdin.readline().split()))


N, = read()
tree = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = read()
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)
labels = read()
goals = read()
res = []


def dfs(root, par, xor0, xor1, depth):
    if depth == 0:
        if labels[root] ^ xor0 != goals[root]:
            res.append(root)
            xor0 ^= 1
    if depth == 1:
        if labels[root] ^ xor1 != goals[root]:
            res.append(root)
            xor1 ^= 1
    for v in tree[root]:
        if v != par:
            yield (v, root, xor0, xor1, depth ^ 1)


stack = [(0, -1, 0, 0, 0)]
while stack:
    for item in dfs(*stack.pop()):
        stack.append(item)

print(len(res))
for x in res:
    print(x + 1)
