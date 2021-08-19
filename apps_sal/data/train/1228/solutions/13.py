t = int(input())
for _ in range(t):
    N = int(input())
    m = []
    n = []
    for _ in range(4 * N - 1):
        (x, y) = map(int, input().split())
        m.append(x)
        n.append(y)
    for i in m:
        if m.count(i) != 2:
            a = i
    for i in n:
        if n.count(i) != 2:
            b = i
    print(a, b)
