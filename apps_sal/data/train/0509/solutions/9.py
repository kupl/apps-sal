from collections import deque


def solve(start, adj):
    N = len(adj)
    ans = [0] * N
    ans[start] = 1
    que = deque([start])
    visited = set()
    while que:
        frm = que.popleft()
        visited.add(frm)
        for to, c in adj[frm]:
            if to in visited:
                continue
            if ans[frm] == c:
                ans[to] = c % N + 1
            else:
                ans[to] = c
            que.append(to)
    return ans


def main():
    N, M = list(map(int, input().split()))
    adj = {i: list() for i in range(N)}
    for i in range(M):
        u, v, c = list(map(int, input().split()))
        adj[u - 1].append((v - 1, c))
        adj[v - 1].append((u - 1, c))
    ans = solve(0, adj)
    for a in ans:
        print(a)


def __starting_point():
    main()


__starting_point()
