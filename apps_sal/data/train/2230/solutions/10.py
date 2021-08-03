n = int(input())
p = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = int(input())
queue = list(map(int, input().split()))
pointers = [[0 for i in range(3)] for j in range(3)]
t = [[list() for i in range(3)] for j in range(3)]
for i in range(n):
    t[a[i] - 1][b[i] - 1].append(p[i])
for i in range(3):
    for j in range(3):
        t[i][j].sort()
for i in range(m):
    m1 = 10 ** 10
    m2 = 10 ** 10
    for j in range(3):
        if len(t[queue[i] - 1][j]) and pointers[queue[i] - 1][j] < len(t[queue[i] - 1][j]) and \
           t[queue[i] - 1][j][pointers[queue[i] - 1][j]] < m1:
            m1 = t[queue[i] - 1][j][pointers[queue[i] - 1][j]]
            pos_j = j
    for j in range(3):
        if len(t[j][queue[i] - 1]) and pointers[j][queue[i] - 1] < len(t[j][queue[i] - 1]) and \
           t[j][queue[i] - 1][pointers[j][queue[i] - 1]] < m2:
            m2 = t[j][queue[i] - 1][pointers[j][queue[i] - 1]]
            pos_i = j
    if m1 == 10 ** 10 and m2 == 10 ** 10:
        print(-1, end=' ')
    elif m1 < m2:
        pointers[queue[i] - 1][pos_j] += 1
        print(m1, end=' ')
    else:
        pointers[pos_i][queue[i] - 1] += 1
        print(m2, end=' ')
