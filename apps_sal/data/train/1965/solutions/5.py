class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        roots = [i for i in range(n)]

        def find(u):
            if u != roots[u]:
                roots[u] = find(roots[u])
            return roots[u]

        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv:
                return False
            roots[max(pu, pv)] = min(pu, pv)
            return True

        edges = sorted(edges, reverse=True)
        i = 0
        connect_times = 0
        to_remove = 0
        while i < len(edges):
            e = edges[i]
            if e[0] != 3:
                break

            res = union(e[1] - 1, e[2] - 1)
            if res == True:
                connect_times += 1
            else:
                to_remove += 1

            i += 1

        origin_roots = deepcopy(roots)
        origin_connect = connect_times
        while i < len(edges):
            e = edges[i]
            if e[0] != 2:
                break

            res = union(e[1] - 1, e[2] - 1)
            if res == True:
                connect_times += 1
            else:
                to_remove += 1

            i += 1
        if connect_times != n - 1:
            return -1

        connect_times = origin_connect
        roots = origin_roots
        while i < len(edges):
            e = edges[i]

            res = union(e[1] - 1, e[2] - 1)
            if res == True:
                connect_times += 1
            else:
                to_remove += 1

            i += 1

        if connect_times != n - 1:
            return -1

        return to_remove
