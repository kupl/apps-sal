for _ in range(int(input())):
    n = int(input())
    x = []
    y = []
    for i in range(4 * n - 1):
        (a, b) = input().split()
        if a in x:
            x.remove(a)
        else:
            x.append(a)
        if b in y:
            y.remove(b)
        else:
            y.append(b)
    print(x[0], y[0])
