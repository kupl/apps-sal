s = list(map(int, input().split()))
n, m = s[0], s[1]
if m == 0:
    print(-1)
    return
g = [[] for i in range(n)]

for i in range(m):
    s = list(map(int, input().split()))
    g[s[0] - 1].append(s[1] - 1)
    g[s[1] - 1].append(s[0] - 1)

vc1 = []
vc2 = []
colors = [-1 for i in range(n)]

for i in range(n):
    if colors[i] != -1:
        continue
    stack = [(i, 1)]
    colors[i] = 1
    while len(stack) > 0:
        s = stack.pop()
        if s[1] == 1:
            vc1.append(s[0] + 1)
        else:
            vc2.append(s[0] + 1)
        for j in g[s[0]]:
            if colors[j] == -1:
                stack.append((j, s[1] ^ 1))
                colors[j] = s[1] ^ 1
            elif colors[j] == s[1]:
                print(-1)
                return
print(len(vc2))
for i in vc2:
    print(i, end=' ')
print("\n", len(vc1), sep='')
for i in vc1:
    print(i, end=' ')
print()

