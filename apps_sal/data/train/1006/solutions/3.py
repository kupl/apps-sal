t = int(input())

while t:
    t = t - 1
    n, d = input().split()
    n = list(n)
    d = int(d)

    n = list(map(int, n))

    x = []
    n.reverse()

    z = 0
    cc = d
    for c in n:
        # print(c, cc, z)
        if c > cc:
            z += 1
        else:
            x.append(c)
            cc = c

    x.reverse()

    for _ in range(z):
        x.append(d)
    x = list(map(str, x))
    print("".join(x))
