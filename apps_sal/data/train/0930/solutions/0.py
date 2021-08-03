for i in range(int(input())):
    t = int(input())
    n = 0
    for i in range(1, t + 1):
        n = n + i
        x = [n]
        y = n
        for j in range(i, t + i - 1):
            if j < t:
                z = y + j
            else:
                z = y + (2 * t - j - 1)
            x.append(z)
            y = z
        print(*x)
