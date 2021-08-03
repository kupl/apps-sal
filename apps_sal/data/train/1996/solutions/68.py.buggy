#[Runtime: 736 ms, faster than 57.43%] DFS
#O(V + E)
from collections import defaultdict
UNKNOWN, VISITING, VISITED = 0, -1, 1
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = defaultdict(int)
        def dfs(cur: int) -> bool:
            \"\"\"return True if there is cycle\"\"\"
            if visited[cur] == VISITED:
                return False
            elif visited[cur] == VISITING:
                return True
            visited[cur] = VISITING
            if any(dfs(nxt) for nxt in graph[cur]):
                return True
            visited[cur] = VISITED
            return False
        return [i for i in range(len(graph)) if not dfs(i)]
