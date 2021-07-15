import math
import queue

class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        if len(initial) == 0:
            return 0
        best = None
        best_val = math.inf
    
        initial_set = set(initial)
        for index in initial:
            initial_set.remove(index)
            
            seen = set()
            Q = queue.Queue()
            for elt in initial_set:
                seen.add(elt)
                Q.put(elt)
            
            while not Q.empty():
                u = Q.get()
                
                for i, v in enumerate(graph[u]):
                    if v == 0 or i in seen:
                        continue 
                    
                    seen.add(i)
                    Q.put(i)
            if len(seen) < best_val:
                best_val = len(seen)
                best = index
            elif len(seen) == best_val and index < best:
                best = index
            initial_set.add(index)
        return best
                    
                    
            
            

