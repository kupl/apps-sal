class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        notSafe = set()
        safe = set()

        def isSafe(node, visited):
            if node in notSafe:
                return False
            if not graph[node]:
                return True
            if node in safe:
                return True
            visited.add(node)
            for child in graph[node]:
                if child in visited:
                    notSafe.add(child)
                    notSafe.add(node)
                    return False
                if not isSafe(child, set(visited)):
                    notSafe.add(child)
                    notSafe.add(node)
                    return False
            safe.add(node)
            return True
        out = []
        for i in range(len(graph)):
            if isSafe(i, set()):
                out += i,
        return out
