I = int(1e+16)
(c, f) = [int(i) for i in input().split()]
arr = [[0 for i in range(c)] for j in range(c)]
sdc = []
for x in range(f):
    sdc.append(list((int(x) for x in input().split())))
for i in sdc:
    arr[i[0] - 1][i[1] - 1] = i[2]
    arr[i[1] - 1][i[0] - 1] = i[2]
for x in range(c):
    for y in range(c):
        if x != y:
            if arr[x][y] == 0:
                arr[x][y] = I


def f_w(v, arr):
    for k in range(0, v):
        for i in range(0, v):
            for j in range(0, v):
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])


f_w(c, arr)
m = -1
for x in range(c):
    m = max(m, max(arr[x]))
print(m)
