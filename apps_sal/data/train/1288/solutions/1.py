t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    mat = [[0 for i in range(n + 1)] for j in range(n + 1)]
    for i in range(m):
        u, v = map(int, input().split())
        mat[u][v] = 1
        mat[v][u] = 1
    ord = []
    for i in range(n + 1):
        ord.append([sum(mat[i]), i])
    ord.sort(reverse=True)
    moves = []
    tld = 0
    ord = ord[:-1]
    for k in range(n):
        mv = 0
        for i in range(n):
            loc = ord[(i + k) % n][1]
            if(mat[loc][0] != 1):
                mv += 1
                for j in range(1, n + 1):
                    if(mat[loc][j] == 1 and mat[j][0] != 1):
                        mat[j][0] = 1
        moves.append(mv)
    print(min(moves))
