from collections import defaultdict
import queue

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        d = defaultdict(set)
        visited = set()
        for edge in edges:
            d[edge[0]].add(edge[1])
            d[edge[1]].add(edge[0])
        q = queue.Queue()
        q.put((1, 0, 1.0))
        visited.add(1)
        goal = {}
        
        while not q.empty():
            cur, time, p = q.get()
            if time > t:
                if target in goal:
                    return goal[target]
                return 0.0
            if cur == target and time == t:
                return p
            c = 0
            for adj in d[cur]:
                if adj not in visited:
                    c += 1
            if c == 0:
                goal[cur] = p
                continue
            for adj in d[cur]:
                if adj not in visited:
                    q.put((adj, time + 1, p / c))
                    visited.add(adj)
        
        if target in goal:
            return goal[target]
        return 0.0

