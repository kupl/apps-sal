class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        
        combined = collections.defaultdict(lambda: [set(), set()])
        
        for i,j in red_edges:
            combined[i][0].add(j)
        for i,j in blue_edges:
            combined[i][1].add(j)
            
        ans = collections.defaultdict(lambda: float('inf'))
            
        # 0 = red, 1 = blue
        
        def bfs(queue):
            seen = set()
            while queue:
                size = len(queue)
                for _ in range(size):
                    cur, distance, color = queue.popleft()
                    ans[cur] = min(ans[cur], distance)
                    for nb in combined[cur][color]:
                        if (cur,nb,color) not in seen:
                            seen.add((cur,nb,color))
                            queue.append((nb, distance + 1, abs(1-color)))
        
        bfs(collections.deque([(0,0,0)]))
        bfs(collections.deque([(0,0,1)]))
        
        return [-1 if i not in ans else ans[i] for i in range(n)]
                    
                
                

