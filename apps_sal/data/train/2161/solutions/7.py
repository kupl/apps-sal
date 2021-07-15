def inp():
    return [int(x) for x in input().split()]


def dfs(u, adj, visited, s, W, B):
    visited[u] = True
    total_w = W[u]
    total_b = B[u]
    s.append(u)
    for v in adj[u]:
        if not visited[v]:
            w, b = dfs(v, adj, visited, s, W, B)
            total_w += w
            total_b += b
    return total_w, total_b


def main():
    n, m, w = inp()
    W = inp()
    B = inp()
    adj = [[] for _ in range(n)]
    for _ in range(m):
        x, y = inp()
        x -= 1
        y -= 1
        adj[x].append(y)
        adj[y].append(x)
    visited = [False] * n
    f = [0] * (w + 1)
    for i in range(n):
        if visited[i]:
            continue
        s = []
        total_w, total_b = dfs(i, adj, visited, s, W, B)
        for j in range(w, -1, -1):
            jw = j + total_w
            if jw <= w:
                f[jw] = max(f[jw], f[j] + total_b)
            for v in s:
                jw = j + W[v]
                if jw <= w:
                    f[jw] = max(f[jw], f[j] + B[v])
    print(f[w])


def __starting_point():
    main()


__starting_point()
