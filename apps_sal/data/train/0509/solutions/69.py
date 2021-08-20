import sys
from collections import deque
from heapq import heappush, heappop


def input():
    return sys.stdin.readline().strip()


def main():
    (N, M) = list(map(int, input().split()))
    repn = [[] for _ in range(N + 1)]
    for _ in range(M):
        (u, v, c) = list(map(int, input().split()))
        repn[u].append((c, v))
        repn[v].append((c, u))
    '\n    グラフにおける構築問題、spanning treeを考えるとうまくいくのは王道なのか？\n    最小全域木はプリムでいいのかな、随分久しぶりに使う。\n\n    木が作れたら、根から順番にラベル付を行う。\n    例えばある親ノードpから辺ラベルcのついた辺で降りてきた頂点vを考えるとき、\n    頂点vにはラベルcをつける。そして子に順々と下っていく。\n    最初の根につけるラベルは、根から伸びるどの辺のラベルとも一致しないラベルを付ければ良い。\n    これは木の辺が頂点数より１小さいことから必ずできることが保証される！\n\n    注意点として、親の親から連続で辺のラベルが連続で一致する場合、この作戦だと\n    親と子で頂点のラベルが一致するので辺が切れてしまう。\n    なのでこの場合だけ子には親と違うラベルをランダムに当てる。\n    '
    visited = [0] * (N + 1)
    used_edge = [[] for _ in range(N + 1)]
    edge_q = []
    for (c, v) in repn[1]:
        heappush(edge_q, (c, 1, v))
    visited[1] = 1
    while edge_q:
        (c, u, v) = heappop(edge_q)
        if visited[v]:
            continue
        visited[v] = 1
        used_edge[u].append((c, v))
        for (nc, nv) in repn[v]:
            if not visited[nv]:
                heappush(edge_q, (nc, v, nv))
    label = [0] * (N + 1)
    cand = set(range(1, N + 1))
    for (c, v) in used_edge[1]:
        cand.discard(c)
    label[1] = cand.pop()
    q = deque()
    for (c, v) in used_edge[1]:
        q.append((c, 1, v))
    while q:
        (c, u, v) = q.popleft()
        if label[u] == c:
            label[v] = 1 if c != 1 else 2
        else:
            label[v] = c
        for (nc, nv) in used_edge[v]:
            q.append((nc, v, nv))
    for (i, l) in enumerate(label):
        if i == 0:
            continue
        print(l)


def __starting_point():
    main()


__starting_point()
