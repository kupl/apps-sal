n = int(input())

p = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

s = []
for i in range(n):
    s.append([p[i], a[i], b[i]])

s = sorted(s)

m = int(input())
c = [int(i) for i in input().split()]

idx = [0] * 4

ans = []

for i in range(m):
    ci = c[i]
    while idx[ci] < n:
        if s[idx[ci]][1] == ci or s[idx[ci]][2] == ci:
            s[idx[ci]][1] = 0
            s[idx[ci]][2] = 0
            ans.append(s[idx[ci]][0])
            break
        idx[ci] += 1
    if idx[ci] == n:
        ans.append(-1)

print(*ans)
