def bfs(mat, x, y, n):
    queue = [[x, y, 0]]
    mark = {j: {u: False for u in range(n)} for j in range(3)}
    n -= 1
    while queue:
        q = queue.pop(0)
        a, b, c = q[0], q[1], q[2]
        if mark[a][b] == True:
            continue
        mark[a][b] = True
        if b == n:
            return 'YES'
        c += 2
        e, r, f = 0, 0, 0
        p = min(b - 1 + c, n)
        z = min(b + 2 + c, n)
        for i in range(p, z):
            if mat[0][i] != '.':
                e = 1
            if mat[1][i] != '.':
                r = 1
            if mat[2][i] != '.':
                f = 1
        if mat[a][p] == '.' or p == n:
            if e == 0:
                if a == 1 or a == 0:
                    if mark[0][b + 1] == False:
                        queue.append([0, b + 1, c])
            if r == 0:
                if mark[1][b + 1] == False:
                    queue.append([1, b + 1, c])
            if f == 0:
                if a == 1 or a == 2:
                    if mark[2][b + 1] == False:
                        queue.append([2, b + 1, c])


t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    mat = {j: {u: x for u, x in enumerate(input())} for j in range(3)}
    if mat[0][0] == 's':
        res = bfs(mat, 0, 0, n)
    elif mat[1][0] == 's':
        res = bfs(mat, 1, 0, n)
    else:
        res = bfs(mat, 2, 0, n)
    if res == None:
        print('NO')
    else:
        print('YES')
