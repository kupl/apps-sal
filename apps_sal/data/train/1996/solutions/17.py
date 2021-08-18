class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        nodes = set()
        for i in range(len(graph)):
            if len(graph[i]) == 0:
                nodes.add(i)

        stop = False
        while not stop:
            tmp = set()
            for i in range(len(graph)):
                if i not in nodes:
                    add = True
                    for dest in graph[i]:
                        if dest not in nodes:
                            add = False
                            break
                    if add:
                        tmp.add(i)
            if len(tmp) == 0:
                stop = True
            nodes = nodes.union(tmp)

        return sorted(nodes)
