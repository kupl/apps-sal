class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(key=lambda x: (-x[0], x[1]))
        removed = set()

        def find_root(parents, i):
            if parents[i] == i:
                return (i, 0)
            (a, b) = find_root(parents, parents[i])
            return (a, b + 1)

        def uf(n, edges, types):
            parents = [x for x in range(n + 1)]
            group = 1
            for (type, a, b) in edges:
                if type not in types:
                    continue
                (r_a, n_a) = find_root(parents, a)
                (r_b, n_b) = find_root(parents, b)
                if r_a != r_b:
                    if n_a >= n_b:
                        parents[r_b] = r_a
                    else:
                        parents[r_a] = r_b
                    group += 1
                else:
                    removed.add((type, a, b))
            return group == n
        if not uf(n, edges, [3, 1]):
            return -1
        if not uf(n, edges, [3, 2]):
            return -1
        return len(removed)
