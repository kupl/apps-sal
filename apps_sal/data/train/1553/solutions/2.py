# cook your dish here
n, m = map(int, input().split())
forest = []
matrix = []
for _ in range(n):
    forest.append(list(map(int, input().split())))
    matrix.append([0] * m)
matrix[0][0] = forest[0][0]
for j in range(1, m):
    matrix[0][j] = matrix[0][j - 1] + forest[0][j]
for i in range(1, n):
    matrix[i][0] = matrix[i - 1][0] + forest[i][0]
for i in range(1, n):
    for j in range(1, m):
        matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1] - matrix[i - 1][j - 1] + forest[i][j]
c = int(input())
for _ in range(c):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    appo = 0
    if x1 > 0:
        appo += matrix[x1 - 1][y2]
    if y1 > 0:
        appo += matrix[x2][y1 - 1]
    if x1 > 0 and y1 > 0:
        appo -= matrix[x1 - 1][y1 - 1]
    print(matrix[x2][y2] - appo)
