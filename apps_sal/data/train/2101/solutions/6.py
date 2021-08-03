class UnionFind(object):
    __slots__ = ['nodes']

    def __init__(self, n: int):
        self.nodes = [-1] * n

    def size(self, x: int) -> int:
        return -self.nodes[self.find(x)]

    def find(self, x: int) -> int:
        if self.nodes[x] < 0:
            return x
        else:
            self.nodes[x] = self.find(self.nodes[x])
            return self.nodes[x]

    def unite(self, x: int, y: int) -> bool:
        root_x, root_y, nodes = self.find(x), self.find(y), self.nodes

        if root_x != root_y:
            if nodes[root_x] > nodes[root_y]:
                root_x, root_y = root_y, root_x
            nodes[root_x] += nodes[root_y]
            nodes[root_y] = root_x

        return root_x != root_y


def main():
    import sys
    from collections import Counter
    n, m = map(int, input().split())
    rev_edges = [[] for _ in range(n)]

    for s, t in (map(int, l.split()) for l in sys.stdin):
        if s < t:
            rev_edges[t - 1].append(s - 1)
        else:
            rev_edges[s - 1].append(t - 1)

    uf = UnionFind(n)
    find, unite, size = uf.find, uf.unite, uf.size
    zero_union = set()

    for v in range(n):
        cnt = Counter()
        for src in rev_edges[v]:
            cnt[find(src)] += 1

        for zero_v in zero_union:
            root = find(zero_v)
            if size(root) > cnt[root]:
                unite(root, v)

        zero_union = set(find(v_) for v_ in zero_union) | {find(v)}

    print(len(zero_union) - 1)


main()
