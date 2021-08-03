n, m = map(int, input().split())
mat = []
for i in range(n):
    me = [int(i) for i in list(input())]
    mat.append(me)
dummy = [[0 for i in range(m + 1)] for j in range(n + 1)]
q = int(input())
for i in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    dummy[x1 - 1][y1 - 1] += 1
    dummy[x2][y1 - 1] -= 1
    dummy[x2][y2] += 1
    dummy[x1 - 1][y2] -= 1
for i in range(n + 1):
    for j in range(m + 1):
        if j == 0:
            continue
        else:
            dummy[i][j] += dummy[i][j - 1]
for j in range(m + 1):
    for i in range(n + 1):
        if i == 0:
            continue
        else:
            dummy[i][j] += dummy[i - 1][j]
for i in range(n):
    for j in range(m):
        print((mat[i][j] + dummy[i][j] + 2) % 2, end="")
    print()
print()
