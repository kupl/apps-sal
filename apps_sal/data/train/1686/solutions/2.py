r, c, k = map(int, input().split())
matrix = []
for _ in range(r):
    matrix.append(list(map(int, input().split())))
left = [[[0, 0] for _ in range(c)] for i in range(r)]
up = [[[0, 0] for _ in range(c)] for i in range(r)]
left[0][0][0] = 1
up[0][0][0] = 1
for i in range(1, min(k + 1, c)):
    if matrix[0][i] == 1:
        left[0][i][0] = left[0][i - 1][0]
        if left[0][i - 1][0] > 0:
            left[0][i][1] = left[0][i - 1][1] + 1
for i in range(1, min(k + 1, r)):
    if matrix[i][0] == 1:
        up[i][0][0] = up[i - 1][0][0]
        if up[i - 1][0][0] > 0:
            up[i][0][1] = up[i - 1][0][1] + 1
for i in range(1, min(k + 1, r)):
    for j in range(1, min(k + 1, c)):
        if matrix[i][j] == 1:
            left[i][j][0] = left[i][j - 1][0] + up[i][j - 1][0]
            if left[i][j - 1][0] + up[i][j - 1][0] > 0:
                left[i][j][1] = left[i][j - 1][1] + 1
            up[i][j][0] = up[i - 1][j][0] + left[i - 1][j][0]
            if left[i - 1][j][0] + up[i - 1][j][0] > 0:
                up[i][j][1] = up[i - 1][j][1] + 1
    for j in range(min(k + 1, c), c):
        if matrix[i][j] == 1:
            up[i][j][0] = up[i - 1][j][0] + left[i - 1][j][0]
            if left[i - 1][j][0] + up[i - 1][j][0] > 0:
                up[i][j][1] = up[i - 1][j][1] + 1
            left[i][j][0] = left[i][j - 1][0] + up[i][j - 1][0]
            if left[i][j - 1][0] + up[i][j - 1][0] > 0:
                left[i][j][1] = left[i][j - 1][1] + 1
            if left[i][j][1] > k:
                left[i][j][0] -= up[i][j - k - 1][0]

for i in range(min(k + 1, r), r):
    for j in range(1, min(k + 1, c)):
        if matrix[i][j] == 1:
            left[i][j][0] = left[i][j - 1][0] + up[i][j - 1][0]
            if left[i][j - 1][0] + up[i][j - 1][0] > 0:
                left[i][j][1] = left[i][j - 1][1] + 1
            up[i][j][0] = up[i - 1][j][0] + left[i - 1][j][0]
            if left[i - 1][j][0] + up[i - 1][j][0] > 0:
                up[i][j][1] = up[i - 1][j][1] + 1
            if up[i][j][1] > k:
                up[i][j][0] -= left[i - k - 1][j][0]

    for j in range(min(k + 1, c), c):
        if matrix[i][j] == 1:
            up[i][j][0] = up[i - 1][j][0] + left[i - 1][j][0]
            if left[i - 1][j][0] + up[i - 1][j][0] > 0:
                up[i][j][1] = up[i - 1][j][1] + 1
            if up[i][j][1] > k:
                up[i][j][0] -= left[i - k - 1][j][0]
            left[i][j][0] = left[i][j - 1][0] + up[i][j - 1][0]
            if left[i][j - 1][0] + up[i][j - 1][0] > 0:
                left[i][j][1] = left[i][j - 1][1] + 1
            if left[i][j][1] > k:
                left[i][j][0] -= up[i][j - k - 1][0]
'''
for i in range(r):
    print([el for el in up[i]])
for i in range(r):
    print([el[0] for el in left[i]])
'''
print((up[-1][-1][0] + left[-1][-1][0]) % 20011)
