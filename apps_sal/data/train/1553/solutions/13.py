# cook your dish here
try:
    m, n = list(map(int, input().split()))
    vol = [[0] * (n + 1)]
    area = [[]]
    for i in range(m):
        area.append([0] + list(map(int, input().split())))
        vol.append([0] * (n + 1))

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            vol[i][j] = vol[i - 1][j] + vol[i][j - 1] - vol[i - 1][j - 1] + area[i][j]

    t = int(input())

    for i in range(t):
        x, y, p, q = list(map(int, input().split()))
        print(vol[p][q] - vol[x - 1][q] - vol[p][y - 1] + vol[x - 1][y - 1])

except:
    pass
