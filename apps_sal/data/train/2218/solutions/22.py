n = int(input())
sp = list(map(int, input().split()))

m = int(input())
pos = [-1] * (n + 1)
m1 = 0
mem = []
for i in range(m):
    sp1 = list(map(int, input().split()))
    mem.append(sp1)
    if sp1[0] == 1:
        sp[sp1[1] - 1] = sp1[2]
        pos[sp1[1] - 1] = i
    else:
        m1 = max(m1, sp1[1])

maxs = [-1] * (m + 1)

for i in range(m - 1, -1, -1):
    sp1 = mem[i]

    if (sp1[0] == 2):
        if (i == m - 1 or sp1[1] > maxs[i + 1]):
            maxs[i] = sp1[1]
        else:
            maxs[i] = maxs[i + 1]
    else:
        maxs[i] = maxs[i + 1]
for i in range(n):
    if pos[i] != -1 and sp[i] < maxs[pos[i]]:
        sp[i] = maxs[pos[i]]
    elif pos[i] == -1:
        sp[i] = max(sp[i], maxs[0])
print(*sp)
