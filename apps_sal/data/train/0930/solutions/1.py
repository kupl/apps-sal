for i in range(int(input())):
    n = int(input())
    t = 0
    for i in range(1, n + 1):
        t = t + i
        m = [t]
        k = t
        for j in range(i, n + i - 1):
            if j < n:
                a = k + j
            else:
                a = k + (2 * n - j - 1)
            m.append(a)
            k = a
        print(*m)
