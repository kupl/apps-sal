from heapq import heappop, heappush
from collections import defaultdict
class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        graph = defaultdict(dict)
        for i, j, l in edges: graph[i][j] = graph[j][i] = l
        heap_queue = [(-M, 0)]
        seen = defaultdict(int)
        while heap_queue:
            move, s = heappop(heap_queue)
            if s in seen: continue
            seen[s] = - move
            for child in graph[s]:
                if child in seen: continue
                nxt_move = - move - graph[s][child] - 1
                if nxt_move >= 0: heappush(heap_queue, (-nxt_move, child))
        result = len(seen)
        for i, j, l in edges: result += min(seen.get(i, 0) + seen.get(j, 0), l)
        return result
