def f_colorful_tree(N, Q, Edges, Queries):
    # 参考: https://atcoder.jp/contests/abc133/submissions/6316420
    # https://atcoder.jp/contests/abc133/submissions/6321437

    import sys
    sys.setrecursionlimit(10**5)

    # 入力は1-basedだが、頂点と色の番号については0-basedで考える(以降も同様)
    tree = [[] for _ in range(N)]
    for a, b, c, d in Edges:
        tree[a - 1].append((b - 1, c - 1, d))
        tree[b - 1].append((a - 1, c - 1, d))

    """Least Common Ancestorを求めるための前処理"""
    depth_from_root = [0] * N
    # [k][v]: 頂点vから2**k個根に近づいたときの頂点番号(根の親は-1とする)
    # 頂点数Nが最大 10**5 なので、2**k >= 10**5 となる k=17 までリストを確保する
    parent_to_root = [[-1] * N for _ in range(18)]
    distance_from_root = [0] * N

    def dfs1(parent, current, depth, distance):
        depth_from_root[current] = depth
        parent_to_root[0][current] = parent
        distance_from_root[current] = distance
        for child, _, dist in tree[current]:  # 色についての情報は必要ない
            if child != parent:
                dfs1(current, child, depth + 1, distance + dist)

    dfs1(-1, 0, 0, 0)
    for i in range(17):
        for j in range(N):
            parent_to_root[i + 1][j] = parent_to_root[i][parent_to_root[i][j]]

    def least_common_ancestor(a, b):
        # editorialと同じことをやる
        if depth_from_root[a] > depth_from_root[b]:
            a, b = b, a
        for i in range(18):
            if (depth_from_root[b] - depth_from_root[a]) & (1 << i):
                b = parent_to_root[i][b]
        if a == b:
            return a
        for i in range(18)[::-1]:
            if parent_to_root[i][a] != parent_to_root[i][b]:
                a = parent_to_root[i][a]
                b = parent_to_root[i][b]
        return parent_to_root[0][a]

    """先読みした(オフライン)クエリに対して解を求める"""
    ans = [0] * Q
    v_need = [[] for i in range(N)]
    for i, (x, y, u, v) in enumerate(Queries):
        # 色xの辺の距離を一律yに変更したとき、頂点u-v間の距離を求める
        lca = least_common_ancestor(u - 1, v - 1)
        # 色の情報を必要としているのは u, v, lca の3点
        # それぞれの点に対して以下の情報を格納する
        # (何番目のクエリか, どの色の距離を変えるか, 変える距離はいくらか, 係数)
        # 係数は u-v間の距離 = 根-u + 根-v - 2 * 根-LCA(u, v) であることを反映
        v_need[u - 1].append((i, x - 1, y, 1))
        v_need[v - 1].append((i, x - 1, y, 1))
        v_need[lca].append((i, x - 1, y, -2))

    color_appear = [0] * N  # [c]: 今訪れている頂点までに色cは何回現れたか
    color_distance = [0] * N  # [c]: 今訪れている頂点まででの色cの辺の距離の和

    def dfs2(parent, current):
        nonlocal color_distance
        for i, x, y, coefficient in v_need[current]:
            ans[i] += (coefficient * (distance_from_root[current] -
                                      color_distance[x] + y * color_appear[x]))
        for child, x, y in tree[current]:
            if child == parent:
                continue
            color_appear[x] += 1
            color_distance[x] += y
            dfs2(current, child)
            # 例えば a→b→c→b→d と移動したことを a→b→d とみなす
            # (オイラーツアーのようにする)ため、戻ってきたなら引く
            color_appear[x] -= 1
            color_distance[x] -= y

    dfs2(-1, 0)
    return '\n'.join(map(str, ans))


N, Q = [int(i) for i in input().split()]
Edges = [[int(i) for i in input().split()] for j in range(N - 1)]
Queries = [[int(i) for i in input().split()] for j in range(Q)]
print(f_colorful_tree(N, Q, Edges, Queries))
