class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        ev_safe = collections.deque()

        sgraph = defaultdict(set)
        rgraph = defaultdict(set)
        safe = [False] * len(graph)

        for i, nei in enumerate(graph):
            if not nei:
                ev_safe.append(i)
            for out in nei:
                rgraph[out].add(i)
                sgraph[i].add(out)

        while ev_safe:
            node_point2safe = ev_safe.popleft()
            safe[node_point2safe] = True
            for node in rgraph[node_point2safe]:
                graph[node].remove(node_point2safe)
                if len(graph[node]) == 0:
                    ev_safe.append(node)

        return [i for i, v in enumerate(safe) if v]
