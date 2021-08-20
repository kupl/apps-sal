def f_colorful_tree(N, Q, Edges, Queries):
    import sys
    sys.setrecursionlimit(10 ** 5)
    tree = [[] for _ in range(N)]
    for (a, b, c, d) in Edges:
        tree[a - 1].append((b - 1, c - 1, d))
        tree[b - 1].append((a - 1, c - 1, d))
    'Least Common Ancestorを求めるための前処理'
    depth_from_root = [0] * N
    parent_to_root = [[-1] * N for _ in range(18)]
    distance_from_root = [0] * N

    def dfs1(parent, current, depth, distance):
        depth_from_root[current] = depth
        parent_to_root[0][current] = parent
        distance_from_root[current] = distance
        for (child, _, dist) in tree[current]:
            if child != parent:
                dfs1(current, child, depth + 1, distance + dist)
    dfs1(-1, 0, 0, 0)
    for i in range(17):
        for j in range(N):
            parent_to_root[i + 1][j] = parent_to_root[i][parent_to_root[i][j]]

    def least_common_ancestor(a, b):
        if depth_from_root[a] > depth_from_root[b]:
            (a, b) = (b, a)
        for i in range(18):
            if depth_from_root[b] - depth_from_root[a] & 1 << i:
                b = parent_to_root[i][b]
        if a == b:
            return a
        for i in range(18)[::-1]:
            if parent_to_root[i][a] != parent_to_root[i][b]:
                a = parent_to_root[i][a]
                b = parent_to_root[i][b]
        return parent_to_root[0][a]
    '先読みした(オフライン)クエリに対して解を求める'
    ans = [0] * Q
    v_need = [[] for i in range(N)]
    for (i, (x, y, u, v)) in enumerate(Queries):
        lca = least_common_ancestor(u - 1, v - 1)
        v_need[u - 1].append((i, x - 1, y, 1))
        v_need[v - 1].append((i, x - 1, y, 1))
        v_need[lca].append((i, x - 1, y, -2))
    color_appear = [0] * N
    color_distance = [0] * N

    def dfs2(parent, current):
        nonlocal color_distance
        for (i, x, y, coefficient) in v_need[current]:
            ans[i] += coefficient * (distance_from_root[current] - color_distance[x] + y * color_appear[x])
        for (child, x, y) in tree[current]:
            if child == parent:
                continue
            color_appear[x] += 1
            color_distance[x] += y
            dfs2(current, child)
            color_appear[x] -= 1
            color_distance[x] -= y
    dfs2(-1, 0)
    return '\n'.join(map(str, ans))


(N, Q) = [int(i) for i in input().split()]
Edges = [[int(i) for i in input().split()] for j in range(N - 1)]
Queries = [[int(i) for i in input().split()] for j in range(Q)]
print(f_colorful_tree(N, Q, Edges, Queries))
