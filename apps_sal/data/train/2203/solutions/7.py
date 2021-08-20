n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
p = [-1 for i in range(n)]
for i in range(n):
    for j in range(1, n + 1):
        if l[i].count(j) == n - j:
            p[i] = j
            break
if p.count(n - 1) == 2:
    p[p.index(n - 1)] = n
print(' '.join(map(str, p)))
