t = int(input())
for i in range(t):
    p = int(input())
    l = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
    c = 0

    while p >= 1:
        m = []
        for i in l:
            if p >= i:
                m.append(p - i)

        p = min(m)

        c += 1
    print(c)
