for _ in range(int(input())):
    (n, m, k) = map(int, input().split())
    d = {}
    s = 0
    for i in range(k):
        (x, y) = map(int, input().split())
        d[x, y] = 1
        s -= d.get((x - 1, y), -1)
        s -= d.get((x, y - 1), -1)
        s -= d.get((x, y + 1), -1)
        s -= d.get((x + 1, y), -1)
    print(s)
