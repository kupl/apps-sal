class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        cycle = set()
        used = set()

        def do(cur, path=set()):
            if cur in used:
                return True
            if cur in cycle or cur in path:
                return False
            for nxt in graph[cur]:
                if not do(nxt, path | {cur}):
                    cycle.update({cur, nxt})
                    return False
            used.add(cur)
            return True
        return list(filter(do, range(len(graph))))
