for _ in range(int(input())):
    n = int(input())
    m = 1000001
    l = []
    for x in map(int, input().split()):
        l.append(x)
        m = min(m, x)
    s = 0
    for i in l:
        s += m * i
    s -= m * m
    print(s)
