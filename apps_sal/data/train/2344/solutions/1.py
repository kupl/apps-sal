import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    (n, m) = map(int, input().split())
    edges = [0] * m
    for i in range(m):
        edges[i] = tuple(map(int, input().split()))
    used = [0] * (3 * n)
    edgess = []
    check = 0
    for i in range(m):
        if used[edges[i][0] - 1] == used[edges[i][1] - 1] == 0:
            edgess.append(i + 1)
            used[edges[i][0] - 1] = 1
            used[edges[i][1] - 1] = 1
            check += 1
    if check >= n:
        useful = edgess[:n]
        edgess = [str(guy) for guy in useful]
        print('Matching')
        print(' '.join(edgess))
    else:
        indep = []
        for i in range(1, 3 * n + 1):
            if used[i - 1] == 0:
                indep.append(i)
        useful = indep[:n]
        verts = [str(guy) for guy in useful]
        print('IndSet')
        print(' '.join(verts))
