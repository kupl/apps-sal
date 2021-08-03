N, M = map(int, input().split())
UVC = [[int(x)for x in input().split()] for _ in range(M)]

tree = [[] for _ in range(N)]
for u, v, c in UVC:
    u -= 1
    v -= 1
    tree[u].append((v, c))
    tree[v].append((u, c))

result = [0] * N
result[0] = 1  # 適当
stack = [0]
while stack:
    current = stack.pop()
    for child, label in tree[current]:
        if result[child] != 0:
            continue
        stack.append(child)
        if result[current] == label:
            result[child] = label + 1 if label < N else 1
        else:
            result[child] = label

print(*result, sep='\n')
