t = int(input())
l = []
for i in range(t):
    n, k = map(int, input().split())
    can = 0
    if n % 2 == 0:
        can = (n // 2) + (n - (n // 2)) * (k + 1)
    else:
        can = (n // 2) + 1 + (n - (n // 2) - 1) * (k + 1) + 2 * k
    l.append(can)
for x in range(t):
    print(l[x])
