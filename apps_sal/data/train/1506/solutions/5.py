# cook your dish here
def flip(dp, x1, y1, x2, y2, n, m):
    dp[x1][y1] += 1

    if y2 + 1 < m:
        dp[x1][y2 + 1] -= 1

    if x2 + 1 < n:
        dp[x2 + 1][y1] -= 1

    if x2 + 1 < n and y2 + 1 < m:
        dp[x2 + 1][y2 + 1] += 1


def main():
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input())))

    dp = [[0 for j in range(m)] for i in range(n)]
    q = int(input())
    for i in range(q):
        x1, y1, x2, y2 = map(int, input().split())
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        flip(dp, x1, y1, x2, y2, n, m)

    for i in range(n):
        for j in range(1, m):
            dp[i][j] += dp[i][j - 1]

    for i in range(1, n):
        for j in range(m):
            dp[i][j] += dp[i - 1][j]

    for i in range(n):
        for j in range(m):
            if dp[i][j] % 2 == 0:
                print(matrix[i][j], end='')
            else:
                print(int(not matrix[i][j]), end='')

        print()


main()
