class Solution:
    def search(self, graph, key, visited):
        stateList = [[key, 1]]
        while stateList:
            index, color = stateList.pop(0)
            if index in visited:
                if visited[index] != color:
                    return False
                continue
            visited[index] = color
            links = graph[index]
            for link in links:
                stateList.append([link, -color])
        return True
            
    def generateGraph(self, dislikes):
        graph = {}
        for a, b in dislikes:
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append(b)
            graph[b].append(a)
        return graph
    
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = self.generateGraph(dislikes)
        
        visited = {}
        for key in graph:
            if key not in visited:
                if not self.search(graph, key, visited):
                    return False
        return True
