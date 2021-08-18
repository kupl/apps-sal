n, k = list(map(int, input().split()))
y = 0
for i in range(k):
    xs = list(map(int, input().split()))
    m, xs = xs[0], xs[1:]
    if xs[0] == 1:
        j = 0
        while j < m and xs[j] == j + 1:
            j += 1
        m -= j
        y += m
        y += m
    else:
        y += m - 1
        y += m
print(y)
