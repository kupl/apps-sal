from collections import defaultdict
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        self.prob = 0
        mp = defaultdict(set)
        for edge in edges:
            mp[edge[0]].add(edge[1])
            mp[edge[1]].add(edge[0])
        visited = set()
        visited.add(1)
        
        def backtrack(pos: int, nowprob: float, currtime: int, visited: Set[int]):
            if currtime == t:
                if pos == target:
                    self.prob += nowprob
                return
            total_visited = 0
            for edge in mp[pos]:
                if edge in visited:
                    total_visited += 1
            div = len(mp[pos]) - total_visited
            if div == 0:
                if pos == target:
                    self.prob += nowprob
                return
            for edge in mp[pos]:
                if edge not in visited:
                    visited.add(edge)
                    backtrack(edge, nowprob/div, currtime+1, visited)
                    visited.remove(edge)
        
            
        backtrack(1, 1, 0, visited)
        return self.prob
                
            

