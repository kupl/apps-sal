from collections import defaultdict
r, c, n = (int(i) for i in input().split())
dr = defaultdict(int)
dc = defaultdict(int)

for i in range(n):
    x, y = (int(i) for i in input().split())
    dr[x] += 1
    dc[y] += 1

mr = max(dr.values())
mc = max(dc.values())
if 1 not in [r, c]:
    print(mr + mc)
else:
    print(max(mr, mc))
