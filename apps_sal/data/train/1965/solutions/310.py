class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        def find(p, i):
            j = i
            while j != p[j]:
                p[j] = p[p[j]]
                j = p[j]
            p[i] = j
            return j

        def join(p, i, j):
            pi = find(p, i)
            pj = find(p, j)
            p[pi] = pj
        e = collections.defaultdict(list)
        for (t, u, v) in edges:
            e[t].append((u, v))

        def build_mst(p, e):
            remove = 0
            for (u, v) in e:
                (pu, pv) = (find(p, u), find(p, v))
                if pu == pv:
                    remove += 1
                else:
                    join(p, u, v)
            return remove
        p = list(range(n + 1))
        remove = build_mst(p, e[3])
        print(p, remove)
        (p_alice, p_bob) = (p[:], p[:])
        remove_alice = build_mst(p_alice, e[1])
        remove_bob = build_mst(p_bob, e[2])
        if len(set([find(p_alice, i + 1) for i in range(n)])) > 1:
            return -1
        if len(set([find(p_bob, i + 1) for i in range(n)])) > 1:
            return -1
        return remove + remove_alice + remove_bob
