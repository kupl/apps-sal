def __starting_point():
    n = int(input())

    for i in range(n):
        h = list(map(int, input().rstrip().split()))
        N = h[0]
        K = h[1]
        h = list(map(int, input().rstrip().split()))
        t = [0] * (2 * K + 2)
        for i in range(N // 2):
            t[h[i] + h[N - i - 1]] -= 1
            t[h[i] + h[N - i - 1] + 1] += 1
            t[max(h[i], h[N - i - 1]) + K + 1] += 1
            t[min(h[i], h[N - i - 1]) + 1] -= 1
        v = N
        minv = N
        for i in range(2 * K + 2):
            v += t[i]
            if v < minv:
                minv = v
        print(minv)


__starting_point()
