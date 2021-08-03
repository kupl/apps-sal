from collections import deque, namedtuple


def dfs(adj, s, visited):
    dq = deque([s])
    while len(dq) > 0:
        now = dq.pop()
        if visited[now]:
            continue
        visited[now] = 1
        for i in adj[now]:
            if not visited[i]:
                dq.append(i)


def main():
    n, m = map(int, input().strip().split())
    adj, check = [[] for j in range(n + m)], 0
    for i in range(n):
        l = [int(j) for j in input().split()][1:]
        check = max(check, len(l))
        for j in l:
            adj[i].append(n + j - 1)
            adj[n + j - 1].append(i)
    visited, ans = [0 for i in range(n + m)], -1
    if check == 0:
        print(n)
        return
    for i in range(n):
        if not visited[i]:
            dfs(adj, i, visited)
            ans += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
