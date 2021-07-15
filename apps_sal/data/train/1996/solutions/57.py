#[] Graph(Reversed-Topology, outdegree)
#1) node A has no child nodes => A must be stable
#2) All childs of node A are stable => A must be stable
#Solution: Traverse all nodes in reversed topological order (remove nodes with out-degree==0 first)
from collections import defaultdict, deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        revadj, outdegree = defaultdict(list), dict()
        for src, dsts in enumerate(graph):
            for dst in dsts:
                revadj[dst].append(src)
            outdegree[src] = len(dsts)
        q, res = deque([i for i, d in outdegree.items() if d == 0]), []
        while q:
            dst = q.popleft()
            res.append(dst)
            for src in revadj[dst]:
                outdegree[src] -= 1
                if outdegree[src] == 0:
                    q.append(src)
        return sorted(res)
