import sys

n, m = map(int, sys.stdin.readline().strip().split())

arr = []
for i in range(n):
    s = input() + "0"
    temp = []
    for x in s:
        temp += [int(x)]
    arr += [temp]

arr += [[0] * (m + 1)]

add = [[0 for i in range(m + 1)] for j in range(n + 1)]
pref1 = [[0 for i in range(m + 1)] for j in range(n + 1)]
pref2 = [[0 for i in range(m + 1)] for j in range(n + 1)]

q = int(sys.stdin.readline().strip())
for _ in range(q):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    pref2[x1][y1] += 1
    pref2[x2 + 1][y1] -= 1
    pref2[x1][y2 + 1] += -1
    pref2[x2 + 1][y2 + 1] -= -1

for i in range(m):
    for j in range(n):
        if j == 0:
            pref1[j][i] = pref2[j][i]
        else:
            pref1[j][i] = pref1[j - 1][i] + pref2[j][i]

for i in range(n):
    for j in range(m):
        if j == 0:
            add[i][j] += pref1[i][j]
        else:
            add[i][j] = add[i][j - 1] + pref1[i][j]

for i in range(n):
    for j in range(m):
        arr[i][j] += add[i][j]
        arr[i][j] %= 2

for i in range(n):
    for j in range(m):
        print(arr[i][j], end='')
    print('')
