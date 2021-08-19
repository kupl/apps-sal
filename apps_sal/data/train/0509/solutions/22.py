from collections import deque


def solve(N, M, uvc):
    tree_map = [[] for _ in range(N + 1)]
    for (u, v, c) in uvc:
        tree_map[u].append([v, c])
        tree_map[v].append([u, c])
    ans = [0] * (N + 1)
    visited = [False] * (N + 1)
    visited[1] = True
    ans[1] = 1
    dq = deque([1])
    while dq:
        now = dq.popleft()
        for (child, c) in tree_map[now]:
            if visited[child]:
                continue
            visited[child] = True
            if c == ans[now]:
                ans[child] = c % N + 1
            else:
                ans[child] = c
            dq.append(child)
    [print(i) for i in ans[1:]]


def __starting_point():
    (N, M) = map(int, input().split())
    uvc = [[int(i) for i in input().split()] for _ in range(M)]
    solve(N, M, uvc)


__starting_point()
