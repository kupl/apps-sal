(n, k, p) = map(int, input().split())
x = [int(x) for x in input().split()]
l = sorted(set(x))
m = 0
l1 = {l[0]: 0}
for i in range(1, len(l)):
    if l[i] - l[i - 1] > k:
        m += 1
    l1[l[i]] = m
for _ in range(p):
    (a, b) = map(int, input().split())
    (a, b) = (x[a - 1], x[b - 1])
    print('Yes') if l1[a] == l1[b] else print('No')
