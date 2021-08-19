n = int(input())
edges = list((list(map(int, input().split())) for _ in range(n - 1)))
colors = list(map(int, input().split()))
edge_cnt = 0
pnt_cnt = {0: 0}
for (a, b) in edges:
    a -= 1
    b -= 1
    if colors[a] != colors[b]:
        edge_cnt += 1
        pnt_cnt[a] = pnt_cnt.get(a, 0) + 1
        pnt_cnt[b] = pnt_cnt.get(b, 0) + 1
for (k, v) in list(pnt_cnt.items()):
    if v == edge_cnt:
        print('YES')
        print(k + 1)
        break
else:
    print('NO')
