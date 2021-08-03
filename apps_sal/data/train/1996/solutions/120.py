class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        parent_g = collections.defaultdict(list)
        visited = set()
        queue = []
        for i in range(len(graph)):
            if len(graph[i]) == 0:
                queue.append(i)
            for c in graph[i]:
                parent_g[c].append(i)
        while(queue):
            current = queue.pop(0)
            flag = True
            for c in graph[current]:
                if not c in visited:
                    flag = False
                    break
            if flag:
                visited.add(current)
                for p in parent_g[current]:
                    if not p in visited:
                        queue.append(p)
        return sorted(list(visited))
