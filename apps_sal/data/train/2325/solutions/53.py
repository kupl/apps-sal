s = input()
t = input()
q = int(input())
n = len(s)
pre = [0] * (n + 1)
for i in range(n):
    if s[i] == "A":
        pre[i] = pre[i - 1] + 1
    else:
        pre[i] = pre[i - 1]
m = len(t)
p = [0] * (m + 1)
for i in range(m):
    if t[i] == "A":
        p[i] = p[i - 1] + 1
    else:
        p[i] = p[i - 1]

for _ in range(q):
    a, b, c, d = [int(x) - 1 for x in input().split()]

    aa = (pre[b] - pre[a - 1])
    co = (b - a + 1 - aa)
    co += aa * 2

    bb = (p[d] - p[c - 1])
    do = (d - c + 1 - bb)
    do += bb * 2
    co %= 3
    do %= 3
    if co == do:
        print("YES")
    else:
        print("NO")
