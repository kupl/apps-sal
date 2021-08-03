class Solution(object):
    def minMalwareSpread(self, graph, initial):
        def dfs(node, visited):
            for neighbor in range(len(graph[node])):
                if graph[node][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor, visited)

        res, max_size = min(initial), 0
        i_set = set(initial)
        total_visited = set()
        for node in range(len(graph)):
            if node not in total_visited:
                visited = {node}
                dfs(node, visited)
                infected = visited & i_set
                if len(infected) == 1:
                    if len(visited) > max_size or (len(visited) == max_size and list(infected)[0] < res):
                        res = list(infected)[0]
                        max_size = len(visited)
                total_visited |= visited
        return res
