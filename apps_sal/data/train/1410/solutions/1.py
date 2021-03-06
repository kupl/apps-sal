nCr = [[0 for x in range(1001)] for x in range(1001)]
for i in range(0, 1001):
    nCr[i][0] = 1
    nCr[i][i] = 1
for i in range(1, 1001):
    for j in range(1, 1001):
        if i != j:
            nCr[i][j] = nCr[i - 1][j] + nCr[i - 1][j - 1]


def main():
    t = int(input())
    for i in range(t):
        num = 0
        line = input().split(' ')
        s = int(line[0])
        n = int(line[1])
        m = int(line[2])
        k = int(line[3])
        if k > n - 1:
            print('0.000000')
        else:
            j = k
            while j < n and j < m:
                p = int(nCr[m - 1][j])
                q = int(nCr[s - m][n - j - 1])
                num = int(num) + p * q
                j = j + 1
            den = int(nCr[s - 1][n - 1])
            ans = float(num) / den
            print('{0:.11f}'.format(ans))


def __starting_point():
    main()


__starting_point()
