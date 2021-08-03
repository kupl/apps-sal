import sys
from collections import deque
readline = sys.stdin.readline


def main():
    INF = float('inf')

    N = int(readline())
    conn = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = list(map(int, readline().split()))
        a -= 1
        b -= 1
        conn[a].append(b)
        conn[b].append(a)

    dist = [INF] * N
    prev = [-1] * N
    dist[0] = 0
    q = deque([0])
    while q:
        x = q.popleft()
        for y in conn[x]:
            if dist[y] == INF:
                dist[y] = dist[x] + 1
                prev[y] = x
                q.append(y)

    path = deque([])
    t = N - 1
    while t >= 0:
        path.appendleft(t)
        t = prev[t]

    a, b = path[dist[-1] // 2], path[dist[-1] // 2 + 1]
    conn[a].remove(b)
    conn[b].remove(a)

    blacks = 0
    visited_b = [False] * N
    q_b = deque([0])
    visited_b[0] = True
    while q_b:
        x = q_b.popleft()
        blacks += 1
        for y in conn[x]:
            if not visited_b[y]:
                visited_b[y] = True
                q_b.append(y)

    whites = 0
    visited_w = [False] * N
    q_w = deque([N - 1])
    visited_w[N - 1] = True
    while q_w:
        x = q_w.popleft()
        whites += 1
        for y in conn[x]:
            if not visited_w[y]:
                visited_w[y] = True
                q_w.append(y)

    print(("Fennec" if blacks > whites else "Snuke"))


def __starting_point():
    main()


__starting_point()
