import sys
input = sys.stdin.readline
(N, M) = map(int, input().split())
graph1 = [[False] * N for _ in range(N)]
for _ in range(M):
    (a, b) = map(int, input().split())
    graph1[a - 1][b - 1] = True
    graph1[b - 1][a - 1] = True
graph = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i != j and (not graph1[i][j]):
            graph[i].append(j)
checked = [-1] * N
Color = [None] * N


def bfs(start):
    q = [start]
    checked[start] = start
    Color[start] = 0
    color = 0
    Cs = [1, 0]
    while q:
        qq = []
        color ^= 1
        for p in q:
            for np in graph[p]:
                if checked[np] == -1:
                    checked[np] = start
                    Color[np] = color
                    qq.append(np)
                    Cs[color] += 1
                elif checked[np] == start and color != Color[np]:
                    return [-1, -1]
        q = qq
    return Cs


def main():
    Dif = []
    for i in range(N):
        if checked[i] == -1:
            (a, b) = bfs(i)
            if a == -1:
                print(-1)
                return
            Dif.append(abs(a - b))
    dp = [False] * (N + 1)
    dp[0] = True
    for d in Dif:
        for j in reversed(range(d, N + 1)):
            dp[j] = dp[j] or dp[j - d]
    min_dif = 10 ** 15
    S = sum(Dif)
    for j in range(N + 1):
        if dp[j]:
            min_dif = min(min_dif, abs(S - j * 2))
    t1 = (N + min_dif) // 2
    t2 = (N - min_dif) // 2
    print(t1 * (t1 - 1) // 2 + t2 * (t2 - 1) // 2)


def __starting_point():
    main()


__starting_point()
