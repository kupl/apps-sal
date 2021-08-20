T = int(input())
while T > 0:
    T -= 1
    N = int(input())
    Sum = N * (N + 1) // 2
    if Sum % 2 != 0:
        print('0')
    else:
        x = -1 + (1 + 4 * Sum) ** 0.5
        x = x // 2
        m = int(x)
        t = N - m
        left = m * (m + 1) // 2
        right = N * (N + 1) // 2 - left
        if left == right:
            r = N - m
            r = r - 1
            m = m - 1
            t += m * (m + 1) // 2
            t += r * (r + 1) // 2
        print(t)
