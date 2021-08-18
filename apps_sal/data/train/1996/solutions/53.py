class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def check_safe(graph, st, seen, cur):
            if st[cur] != 0:
                return st[cur]
            if len(graph[cur]) == 0:
                return 1
            if cur in seen:
                return -1
            seen.add(cur)
            for ne in graph[cur]:
                rtv = check_safe(graph, st, seen, ne)
                if rtv == -1:
                    st[cur] = -1
                    return -1
            seen.discard(cur)
            st[cur] = 1
            return 1

        N = len(graph)
        st = [0] * N

        for i in range(N):
            if st[i] != 0:
                continue
            seen = set()
            st[i] = check_safe(graph, st, seen, i)
        rtv = []
        for i, s in enumerate(st):
            if s == 1:
                rtv.append(i)
        return rtv
