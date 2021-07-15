class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = collections.defaultdict(list)
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        
        q = [(1, 1, 0)]
        seen = set()
        
        while q:
            curr, p, time = q.pop(0)
            if time >= t:
                if curr == target:
                    return p
                continue 
                
            seen.add(curr)
            s = 0
            for nei in graph[curr]:
                if nei not in seen:
                    s += 1
            if s:
                for nei in graph[curr] :
                    if nei not in seen:
                        q.append((nei, p / s, time + 1))
            else:
                q.append((curr, p, time + 1))
                
        return 0. 

