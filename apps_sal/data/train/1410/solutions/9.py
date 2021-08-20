def main():
    maxN = 1010
    c = [[0] * maxN for x in range(maxN)]
    for i in range(maxN):
        c[i][0] = 1
        c[i][i] = 1
    for i in range(1, maxN):
        for j in range(1, maxN):
            if i != j:
                c[i][j] = c[i - 1][j] + c[i - 1][j - 1]
    t = int(input())
    for i in range(t):
        (s, n, m, k) = list(map(int, input().split(' ')))
        D = float(c[s - 1][n - 1])
        N = 0.0
        if s == n:
            print(1.0)
            continue
        if k > n:
            print(0.0)
            continue
        upper = min(m, n)
        for j in range(k, upper):
            N += c[m - 1][j] * c[s - m][n - 1 - j]
        ans = float(N / D)
        print('%f' % ans)


main()
