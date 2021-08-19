r = int(input())
c = 0
L = []
for i in range(2 * r + 1, 2 * r ** 2 + 2):
    for j in range(i, r ** 4 + 2 * r ** 2 + 2):
        for k in range(j, r ** 4 + 3 * r ** 2 + 2):
            if 4 * (i + j + k) * r ** 2 == (i + j - k) * (i + k - j) * (j + k - i):
                L.append([i, j, k])
                c += 1
print(c)
for i in range(c):
    for j in range(3):
        print(L[i][j], end=' ')
    print()
