for i in range(int(input())):
    n = int(input())
    s = 0
    for i in range(n):
        a, b, c = map(int, input().split())
        d = (c / 100) * a
        e = a + d
        f = e - ((c / 100) * e)
        g = a - f
        h = b * g
        s = s + h
    print(s)
