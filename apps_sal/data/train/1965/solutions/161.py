class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        (parenta, parentb) = ([i for i in range(n)], [i for i in range(n)])

        def find(i, parent):
            if parent[i] != i:
                parent[i] = find(parent[i], parent)
            return parent[i]

        def union(a, b, parent):
            (pa, pb) = (find(a, parent), find(b, parent))
            if pa == pb:
                return False
            parent[pa] = pb
            return True
        added_edge = na = nb = 0
        for (typ, u, v) in edges:
            if typ == 3 and union(u - 1, v - 1, parenta) and union(u - 1, v - 1, parentb):
                added_edge += 1
                na += 1
                nb += 1
        for (typ, u, v) in edges:
            if typ == 1 and union(u - 1, v - 1, parenta):
                added_edge += 1
                na += 1
            elif typ == 2 and union(u - 1, v - 1, parentb):
                added_edge += 1
                nb += 1
        return len(edges) - added_edge if na == nb == n - 1 else -1
