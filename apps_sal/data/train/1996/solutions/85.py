class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        perm = {i for (i, e) in enumerate(graph) if not e}
        rev = [[] for i in range(len(graph))]
        for (i, e) in enumerate(graph):
            for j in e:
                rev[j].append(i)
        last = perm.copy()
        while last:
            tmp = set()
            for n in last:
                for nei in rev[n]:
                    if nei not in perm and all((cat in perm for cat in graph[nei])):
                        tmp.add(nei)
            perm = perm.union(tmp)
            last = tmp
        return sorted(perm)
