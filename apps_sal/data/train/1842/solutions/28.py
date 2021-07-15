class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = collections.defaultdict(set)
        for s, e in edges:
            graph[s].add(e)
            graph[e].add(s)
        
        def dfs(prev_node: int, seconds_left: int, visited: Set[int]):
            if seconds_left == 0 or prev_node not in graph:
                return int(prev_node == target)
            
            probability = 0
            n_next_node = 0
            for next_node in graph[prev_node]:
                if next_node not in visited:
                    probability += dfs(next_node, seconds_left-1, set(list(visited) + [prev_node]))
                    n_next_node += 1
            if n_next_node == 0:
                return int(prev_node == target)
            if probability > 0:
                probability /= n_next_node
            return probability
            
        
        return dfs(prev_node=1, seconds_left=t, visited=())
