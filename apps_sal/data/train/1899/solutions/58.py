class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        num_rows, num_cols = len(A), len(A[0])
        
        def components():
            done = set()
            components = []
            
            for row in range(num_rows):
                for col in range(num_cols):
                    if A[row][col] and (row, col) not in done:
                        stack = [(row, col)]
                        seen = {(row, col)}
                        while stack:
                            curr = stack.pop()
                            for (a,b) in [(1,0),(-1,0),(0,1),(0,-1)]:
                                nei = (curr[0]+a, curr[1]+b)
                                if 0<=nei[0]<num_rows and 0<=nei[1]<num_cols\\
                                and A[nei[0]][nei[1]] and nei not in seen:
                                    stack.append(nei)
                                    seen.add(nei)
                        done |= seen
                        components.append(seen)
                        if len(components)==2:
                            return components
                        
        source, target = components()
        queue = [(node, 0) for node in source]
        done = set(source)
        while queue:
            curr, d = queue.pop(0)
            print(curr)
            if curr in target: return d-1
            for (a,b) in [(1,0),(-1,0),(0,1),(0,-1)]:
                nei = (curr[0] + a, curr[1] + b)
                if 0<=nei[0]<num_rows and 0<=nei[1]<num_cols and nei not in done:
                    queue.append((nei,d+1))
                    done.add(nei)
