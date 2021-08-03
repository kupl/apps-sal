t = eval(input())
for i in range(0, t):
    a = []
    n = eval(input())
    a = input().split()
    for j in range(0, n):
        a[j] = int(a[j])

    a.sort()
    m = 10000000000
    for j in range(0, n - 1):
        if (a[j + 1] - a[j] < m):
            m = (a[j + 1] - a[j])

    print(m)
