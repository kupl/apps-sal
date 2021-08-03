import sys
from array import array  # noqa: F401

n = int(input())
matrix = [array('i', list(map(int, input().split()))) for _ in range(n)]
aa = tuple([int(x) - 1 for x in input().split()])
ans = [''] * n

for i in range(n - 1, -1, -1):
    x = aa[i]

    for a in range(n):
        for b in range(n):
            if matrix[a][b] > matrix[a][x] + matrix[x][b]:
                matrix[a][b] = matrix[a][x] + matrix[x][b]

    val, overflow = 0, 0
    for a in aa[i:]:
        for b in aa[i:]:
            val += matrix[a][b]
        if val > 10**9:
            overflow += 1
            val -= 10**9

    ans[i] = str(10**9 * overflow + val)

print(' '.join(ans))
