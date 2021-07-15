class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        #dfs to find all node in a subgraph, only subgraph with 1 infected node can be saved as we can remove only one node
        init = set(initial)
        total_visited = set()
        res, max_subgraph_len = min(initial), 0
        for node in range(len(graph)):
            if node not in total_visited:
                visited = set([node])
                self.dfsConnected(graph, node, visited)
                #find infected node in subgraph
                infected = visited & init
                if len(infected) == 1:
                    if len(visited) > max_subgraph_len or (len(visited) == max_subgraph_len and min(infected) < res):
                        res, max_subgraph_len = min(infected), len(visited)
                total_visited |= visited
        return res
    
    def dfsConnected(self, graph, node, visited):
        for neighbor in range(len(graph[node])):
            if graph[node][neighbor] == 1 and neighbor not in visited:
                visited.add(neighbor)
                self.dfsConnected(graph, neighbor, visited)
