r = [0, 1, 1, 2, 1, 4, 2, 6, 1, 8, 4]

n, m = [int(x) for x in input().split()]
if m == 1:
    print(r[n])
elif (n + 1) / 2 <= m:
    print(m)
else:
    print(n - m)
