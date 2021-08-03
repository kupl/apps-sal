t = int(input())

while (t > 0):
    n, k = map(int, input().split())
    a = list()
    if 2 * k <= n:
        for i in range(2 * k):
            if i % 2 == 0:
                a.append(i + 1)
            else:
                a.append(-i - 1)
        for i in range(2 * k, n, 1):
            a.append(-i - 1)
    elif 2 * k > n:
        for i in range(2 * (n - k)):
            if i % 2 == 0:
                a.append(i + 1)
            else:
                a.append(-i - 1)
        for i in range(2 * (n - k), n, 1):
            a.append(i + 1)
    else:
        for i in range(2 * k):
            if i % 2 == 0:
                a.append(i + 1)
            else:
                a.append(-i - 1)
    for i in a:
        print(i, end=" ")
    t -= 1
