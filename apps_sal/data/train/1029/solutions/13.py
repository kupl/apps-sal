for i in range(int(input())):
    n, m = [int(i) for i in input().split()]
    l = list(map(int, input().split()))
    g = []
    for i in range(1, n + 1):
        g.append(i)
    un = [each for each in g if each not in l]
    chef = un[::2]
    ass = un[1::2]
    print(*chef)
    print(*ass)
