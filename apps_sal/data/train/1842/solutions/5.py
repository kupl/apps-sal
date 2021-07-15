class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            
        seen = set([1])
        
        queue = collections.deque([(1, 1)])
        
        while t > 0:
            size = len(queue)
            for _ in range(size):
                f, prob = queue.popleft()
                length = 0
                for nb in graph[f]:
                    if nb not in seen:
                        length += 1
                        
                if length == 0:
                    queue.append((f, prob))
                else:
                    for nb in graph[f]:
                        if nb not in seen:
                            seen.add(nb)
                            queue.append((nb, prob / length))
                            
            t -= 1
            
        res = 0
        for node, prob in queue:
            if node == target:
                res += prob
                
        return res

                        
                

