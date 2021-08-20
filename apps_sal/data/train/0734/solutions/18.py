"""
25th march 2019 monday
rocket to the moon
"""
t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = list()
    for (id, x) in enumerate(a):
        b.append([x, id])
    b.sort()
    a.sort()
    counter = list()
    count = 1
    c_max = 1
    for i in range(1, n):
        if a[i] == a[i - 1]:
            count += 1
        else:
            counter.append(count)
            c_max = max(c_max, counter[-1])
            count = 1
    counter.append(count)
    c_max = max(c_max, counter[-1])
    if c_max > n // 2:
        print('No')
    else:
        print('Yes')
        c = [0] * n
        for i in range(n):
            c[b[i][1]] = b[(i + c_max) % n][0]
        for x in c:
            print(x, end=' ')
        print('')
