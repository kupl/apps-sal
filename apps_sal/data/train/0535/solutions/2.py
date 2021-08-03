def ncr(n, r):
    if n < r:
        return 0
    elif r == 2:
        return(n * (n - 1) / 2)
    elif r == 1:
        return n
    else:
        t = 0


t = int(input())
for p in range(t):
    n, m, x, y = input().split()
    n, m, x, y = int(n), int(m), int(x), int(y)

    maxi = ncr(n * m - 1, 2)

    sub1 = ncr(n, 2) * (m - 1)
    sub2 = ncr(m, 2) * (n - 1)
    maxi = maxi - (sub1 + sub2)
    # print(maxi)

    sub3 = ncr(y - 1, 2) + ncr(m - y, 2)
    sub4 = ncr(x - 1, 2) + ncr(n - x, 2)
    # print(sub3,sub4)
    maxi = maxi - (sub3 + sub4)
    # print(maxi)

    if n < m:
        temp = n
        diff = m - n
    else:
        temp = m
        diff = n - m

    sub5 = 0
    sub6 = 0
    for i in range(2, temp):
        sub5 += ncr(i, 2)

    for j in range(diff + 1):
        sub6 += ncr(temp, 2)

    sub5 *= 4
    sub6 *= 2

    # print(sub5,sub6)
    maxi = maxi - (sub5 + sub6)
    # print(maxi)

    l1 = min(n - x, y - 1)
    l2 = min(m - y, x - 1)
    maxi = maxi + l1 + l2 + (l1 * l2)

    l3 = min(x - 1, y - 1)
    l4 = min(m - y, n - x)
    maxi = maxi + l3 + l4 + (l3 * l4)

    print(int(maxi * 2))
