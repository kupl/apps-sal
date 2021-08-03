from bisect import bisect_right
a = list([ord(x) - ord("a") for x in list(input())])
n = len(a)
m = 26

b = [0] * n
pos = [[] for i in range(m)]
s = set()
cnt = 0
for i in reversed(list(range(n))):
    b[i] = cnt
    if a[i] not in s:
        s.add(a[i])
    pos[a[i]].append(i)
    if len(s) == m:
        cnt += 1
        s = set()

for i in range(m):
    pos[i].sort()

k = cnt + 1


ans = []
cur = -1
for i in range(k):
    for j in range(m):
        pj = bisect_right(pos[j], cur)
        if pj == len(pos[j]):
            ans.append(j)
            break
        to = pos[j][pj]
        if b[to] != k - i - 1:
            cur = to
            ans.append(j)
            break

ans = "".join(chr(ord("a") + i) for i in ans)
print(ans)
