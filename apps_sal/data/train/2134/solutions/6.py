n = int(input())
parents = [None] + [int(x) - 1 for x in input().split()]
s = list(map(int, input().split()))
children = [[] for _ in range(n)]
a = [None for _ in range(n)]

for v, parent in enumerate(parents):
    if parent is not None:
        children[parent] += [v]

broken = False
stack = []
stack.append((0, 1))
a[0] = s[0]
while len(stack) > 0:
    v, depth = stack.pop()
    if depth % 2 == 0:
        if len(children[v]) > 0:
            s[v] = s[min(children[v], key=lambda child: s[child])]
        else:
            s[v] = s[parents[v]]
        if s[v] < s[parents[v]]:
            broken = True
            break
    if depth > 1:
        a[v] = s[v] - s[parents[v]]
    for child in children[v]:
        stack.append((child, depth + 1))

if not broken:
    print(sum(a))
else:
    print(-1)
