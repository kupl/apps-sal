a = int(input())
for _ in range(a):
    (c, d) = list(map(int, input().split()))
    crr = [[[0, 0] for i in range(c + 1)] for j in range(c + 1)]
    trr = []
    for i in range(c):
        kk = list(input().split())
        trr.append(kk)
    for i in range(1, c + 1):
        for j in range(1, c + 1):
            if trr[i - 1][j - 1] == 'a':
                crr[i][j][0] = max(crr[i - 1][j][0], crr[i][j - 1][0]) + 1
                if j == 1:
                    crr[i][j][1] = crr[i - 1][j][1] + 1
                elif i == 1:
                    crr[i][j][1] = crr[i][j - 1][1] + 1
                elif crr[i - 1][j][0] > crr[i][j - 1][0]:
                    crr[i][j][1] = crr[i - 1][j][1] + 1
                else:
                    crr[i][j][1] = crr[i][j - 1][1] + 1
            else:
                crr[i][j][0] = max(crr[i - 1][j][0], crr[i][j - 1][0])
                if j == 1:
                    crr[i][j][1] = crr[i - 1][j][1] + 1
                elif i == 1:
                    crr[i][j][1] = crr[i][j - 1][1] + 1
                elif crr[i - 1][j][0] > crr[i][j - 1][0]:
                    crr[i][j][1] = crr[i - 1][j][1] + 1
                else:
                    crr[i][j][1] = crr[i][j - 1][1] + 1
    for i in range(d):
        (m, n) = list(map(int, input().split()))
        print(crr[m][n][1] - crr[m][n][0])
