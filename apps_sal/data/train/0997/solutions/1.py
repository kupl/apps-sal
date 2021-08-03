for _ in range(int(input())):
    n, m = map(int, input().split())

    s = [1] * n + [0]

    for _ in range(m):
        i, j, k = map(int, input().split())

        s[i - 1] *= k
        s[j] /= k

    for i in range(1, n):
        s[i] *= s[i - 1]

    print(int(sum(s) * 10 // n))
