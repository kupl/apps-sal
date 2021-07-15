#[Runtime: 736 ms, faster than 57.43%] DFS
#O(V + E)
from collections import defaultdict
UNKNOWN, VISITING, VISITED = 0, 1, 2
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj, visited = defaultdict(list), defaultdict(int)
        #build graph
        for src, dsts in enumerate(graph):
            for dst in dsts:
                adj[src].append(dst)
        def dfs(cur: int) -> bool:
            \"\"\"return True if there is cycle\"\"\"
            if visited[cur] == VISITED:
                return False
            elif visited[cur] == VISITING:
                return True
            visited[cur] = VISITING
            if any(dfs(nxt) for nxt in adj[cur]):
                return True
            visited[cur] = VISITED
            return False
        return [i for i in range(len(graph)) if not dfs(i)]
