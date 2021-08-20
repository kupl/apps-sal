for _ in range(int(input())):
    n = int(input())
    xloli = []
    hloli = []
    d1 = []
    d2 = []
    for i in range(n):
        (x, h) = (int(x) for x in input().split())
        xloli.append(x)
        hloli.append(h)
    for i in range(1, n):
        d1.append(xloli[i] - xloli[i - 1])
    d2.append(d1[0])
    for i in range(n - 2):
        d2.append(d1[i + 1] + d1[i])
    d2.append(d1[-1])
    kaori = 0
    hloli.sort()
    d2.sort()
    for i in range(n):
        kaori += hloli[i] * d2[i]
    print(kaori)
