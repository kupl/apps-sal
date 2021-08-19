def check_relative(i, j):
    if is_relative[i]:
        return
    if j in direct_relatives[i] or i in direct_relatives[j]:
        is_relative[i] = True
        for ii in range(n):
            check_relative(ii, i)


(n, k) = map(int, input().split())
land = []
is_relative = [False] * n
for i in range(n):
    (p, *q) = input().split()
    land.append(set(q))
direct_relatives = {k: set() for k in range(n)}
for i in range(n):
    for j in range(n):
        if len(land[i].intersection(land[j])) >= k:
            direct_relatives[i].add(j)
for i in range(n):
    check_relative(i, 0)
print(is_relative.count(True))
