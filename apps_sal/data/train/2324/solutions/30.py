from collections import deque

N = int(input())

INF = 100001
G = [[] for i in range(N)]
dist1, dist2 = [INF for j in range(N)], [INF for k in range(N)]


def bfs(s, d):
    check, q = [0 for i in range(N)], deque()
    check[s], d[s] = 1, 0
    q.append(s)

    while len(q) != 0:
        u = q.popleft()
        for i in G[u]:
            if check[i] == 0:
                check[i], d[i] = 1, d[u] + 1
                q.append(i)
        check[u] = 2


def main():
    for i in range(N - 1):
        a, b = list(map(int, input().split()))
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)

    bfs(0, dist1)
    bfs(N - 1, dist2)

    cnt_f = 0
    for i in range(N):
        if dist1[i] <= dist2[i]:
            cnt_f += 1

    if N // 2 < cnt_f:
        print("Fennec")
    else:
        print("Snuke")


def __starting_point():
    main()


__starting_point()
