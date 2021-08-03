class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        adj = {}
        for i in range(n):
            adj[i] = set(graph[i])

        safe = set()
        for i in range(n):
            if not adj[i]:
                safe.add(i)

        prev_size = len(safe)
        while True:
            for i in range(n):
                if i in safe:
                    continue
                for x in adj[i]:
                    if x not in safe:
                        break
                else:
                    safe.add(i)
            if len(safe) == prev_size:
                break
            else:
                prev_size = len(safe)

        out = []
        for i in range(n):
            if i in safe:
                out.append(i)
        return out
