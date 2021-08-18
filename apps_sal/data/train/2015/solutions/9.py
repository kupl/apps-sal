ans = 0
l = []
t = int(input())
for i in range(t):
    n, m, k = list(map(int, input().split()))
    l.append([n, m, k])

ans = 0
p = []
for i in range(t):

    if l[i][2] >= 0:
        k = 0
        v = 0
        for j in range(i + 1, t):
            if l[j][2] >= 0:
                l[j][2] -= (max(0, l[i][0] - k) + v)
                if l[j][2] < 0:
                    v += l[j][1]
                    l[j][1] = 0
                k += 1
        p.append(i + 1)

print(len(p))
print(*p)
