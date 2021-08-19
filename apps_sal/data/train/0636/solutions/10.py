from collections import defaultdict
l = list(map(int, input().split()))
n = l[0]
t = l[1]
l.pop(0)
l.pop(0)
d = defaultdict(list)
cnt = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        s = l[i] + l[j]
        if d[t - s]:
            x = d[t - s]
            for p in x:
                if p[0] < i and p[0] < i < p[1] < j:
                    cnt += 1
        d[s].append([i, j])
print(cnt)
