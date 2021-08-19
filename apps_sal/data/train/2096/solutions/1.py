n = int(input())
a = list(map(int, input().split()))
x = sorted([(a[i], i) for i in range(n)])
cycles = []
was = [False for i in range(n)]
for i in range(n):
    if was[i]:
        continue
    cur = i
    cyc = []
    while not was[cur]:
        was[cur] = True
        cyc.append(cur + 1)
        cur = x[cur][1]
    cycles.append(cyc)
print(len(cycles))
for cyc in cycles:
    print(len(cyc), ' '.join(map(str, cyc)))
