class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        ans = []
        N = len(graph)
        out = collections.defaultdict(set)
        in_cnt = [0 for _ in range(N)]
        ready = set(range(N))
        for end in range(N):
            for start in graph[end]:
                out[start].add(end)
                in_cnt[end] += 1
                if end in ready:
                    ready.remove(end)
        while len(ready) > 0:
            rm = ready.pop()
            ans.append(rm)
            for nei in out[rm]:
                in_cnt[nei] -= 1
                if in_cnt[nei] == 0:
                    ready.add(nei)
        return sorted(ans)
