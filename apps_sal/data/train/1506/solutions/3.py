def issafe(a, b, n, m):
    if(0 <= a < n and 0 <= b < m):
        return True
    return False


def main():
    n, m = map(int, input().split())
    mat = [list(map(int, list(input()))) for i in range(n)]
    qmat = [[0 for i in range(m)] for j in range(n)]
    q = int(input())
    query = [list(map(int, input().split())) for i in range(q)]
    for k in query:
        i1, j1, i2, j2 = map(lambda x: x - 1, k)
        qmat[i1][j1] += 1
        if(issafe(i2 + 1, j2 + 1, n, m)):
            qmat[i2 + 1][j2 + 1] += 1
        if(issafe(i1, j2 + 1, n, m)):
            qmat[i1][j2 + 1] += -1
        if(issafe(i2 + 1, j1, n, m)):
            qmat[i2 + 1][j1] += -1
    for i in range(n - 1):
        for j in range(m):
            qmat[i + 1][j] += qmat[i][j]
    for i in range(n):
        for j in range(m - 1):
            qmat[i][j + 1] += qmat[i][j]
    for i in range(n):
        for j in range(m):
            qmat[i][j] = (qmat[i][j] + mat[i][j]) % 2
    for i in qmat:
        print(*i, sep='')


main()
