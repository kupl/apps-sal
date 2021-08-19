class Solution:

    def isCycle(self, src, graph: List[List[int]], visited):
        (WHITE, GRAY, BLACK) = (0, 1, 2)
        if visited[src] != WHITE:
            return visited[src] == GRAY
        stack = []
        stack.append((src, 1))
        stack.append((src, 0))
        while stack:
            current = stack.pop()
            if current[1] == 1:
                visited[current[0]] = BLACK
                continue
            current = current[0]
            visited[current] = GRAY
            for e in graph[current]:
                if visited[e] == GRAY:
                    return True
                if visited[e] == WHITE:
                    stack.append((e, 1))
                    stack.append((e, 0))
        return False

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        eventualSafe = []
        visited = [0] * len(graph)
        for i in range(len(graph)):
            if not self.isCycle(i, graph, visited):
                eventualSafe.append(i)
        return eventualSafe
