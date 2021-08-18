from collections import defaultdict

N = int(input())
a = [int(i) for i in input().split()]

b = defaultdict(lambda: [float('inf'), 0])
for i in range(N):
    b[a[i]][0] = min(b[a[i]][0], i)
    b[a[i]][1] += 1

c = [(0, 0, 0)]
for k, v in b.items():
    c.append((k, v[0], v[1]))
c.sort()

ret = [0] * N
pre_v, pre_i, pre_c = c.pop()
while c:
    cur_v, cur_i, cur_c = c.pop()
    ret[pre_i] += (pre_v - cur_v) * pre_c
    cur_c += pre_c
    pre_v, pre_i, pre_c = cur_v, min(pre_i, cur_i), cur_c

for r in ret:
    print(r)
