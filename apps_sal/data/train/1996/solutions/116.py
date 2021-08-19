from collections import defaultdict


class Solution:

    def eventualSafeNodes(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        inv = defaultdict(set)
        N = len(edges)
        ret = set()
        for (s, es) in enumerate(edges):
            for e in es:
                graph[s].add(e)
                inv[e].add(s)
        for n in range(N):
            if len(graph[n]) == 0:
                ret.add(n)
        todo = set(ret)
        while todo:
            pending = set()
            for n in todo:
                for s in inv[n]:
                    if graph[s].issubset(ret):
                        ret.add(s)
                        pending.add(s)
            todo = pending
        return sorted(ret)
