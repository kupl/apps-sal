for _ in range(int(input())):
    n = int(input())
    plus = []
    minus = []
    for i in range(n):
        (x, y) = list(map(int, input().split()))
        plus.append(x + y)
        minus.append(x - y)
    (plus.sort(), minus.sort())
    m = float('inf')
    for i in range(1, n):
        if plus[i] - plus[i - 1] < m:
            m = plus[i] - plus[i - 1]
        if minus[i] - minus[i - 1] < m:
            m = minus[i] - minus[i - 1]
    if m % 2 == 0:
        print(m // 2)
    else:
        print(m / 2)
