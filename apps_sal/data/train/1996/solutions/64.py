from collections import defaultdict

class Solution:
    def dfs(self, node, graph, eventuallySafe, visited):
        if node in eventuallySafe:
            return True
        if node in visited:
            return False
        
        # never seen before
        visited.add(node)
        adjNodes = graph[node]
        if len(adjNodes) != 0:
            isEventuallySafe = True
            for neighbour in adjNodes:
                isEventuallySafe = self.dfs(neighbour, graph, eventuallySafe, visited) and isEventuallySafe
            
            if not isEventuallySafe:
                return False

        # eventually safe, or safe
        eventuallySafe.add(node)
        return True

        
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # isSafe(n) <==> n.edges = {}
        # isEventuallySafe(n) <=> for_all e IN n.edges, isEventuallySafe(n) || isSafe(n)
        
        eventuallySafe = set()
        visited = set()
        for n in range(len(graph)):
            self.dfs(n, graph, eventuallySafe, visited)
            
        return sorted(list(eventuallySafe))
            

