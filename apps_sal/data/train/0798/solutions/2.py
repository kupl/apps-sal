# cook your dish here
import sys


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
charms = []
for _ in range(m):
    x, y, lungh = map(int, input().split())
    x -= 1
    y -= 1
    charms.append([x, y, lungh])
if m <= 10:
    for i in range(n):
        for j in range(n):
            flag = 0
            for charm in charms:
                if dist([i, j], charm[:2]) <= charm[2]:
                    flag = 1
                    break
            if flag == 0:
                matrix[i][j] = -float('Inf')
else:
    for charm in charms:
        for i in range(-charm[2], charm[2] + 1):
            appo = charm[2] - abs(i)
            for j in range(-appo, appo + 1):
                if i >= 0 and i < n and j >= 0 and j < n:
                    matrix[i][j] = float('Inf')
for i in range(1, n):
    matrix[0][i] += matrix[0][i - 1]
    matrix[i][0] += matrix[i - 1][0]
for i in range(1, n):
    for j in range(1, n):
        matrix[i][j] += max(matrix[i - 1][j], matrix[i][j - 1])
if matrix[n - 1][n - 1] < -10**(10):
    print('NO')
else:
    print('YES')
    print(matrix[n - 1][n - 1])
