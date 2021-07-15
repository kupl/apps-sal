class Solution:
    
    def transform_island(self, A, i, j, queue, visited):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[i]) or (i, j) in visited:
            return
        
        if A[i][j] == 0:
            return
        
        A[i][j] = float('inf')
        queue.append((0, i, j))
        visited.add((i, j))
        self.transform_island(A, i+1, j, queue, visited)
        self.transform_island(A, i, j+1, queue, visited)
        self.transform_island(A, i-1, j, queue, visited)
        self.transform_island(A, i, j-1, queue, visited)
    
    def shortestBridge(self, A: List[List[int]]) -> int:
        queue = collections.deque([])
        visited = set()
        # find the first 1, and search all its neighbors to turn it into -1
        for i in range(len(A)):
            should_break = False
            for j in range(len(A[i])):
                if A[i][j] == 1:
                    self.transform_island(A, i, j, queue, set())
                    should_break = True
                    break
            if should_break:
                break
        
        # print(A, queue)
        # BFS approach
        while len(queue) > 0:
            prev_val, i, j = queue.popleft()
            next_val = prev_val - 1 # records the amount of steps
            print(('q', i, j, next_val))
            if A[i][j] == 1: # reached the other island
                return -prev_val-1
            
             # push boundary of the island
            if i > 0 and A[i-1][j] >= 0 and (i-1, j) not in visited:
                visited.add((i-1, j))
                queue.append((next_val, i-1, j))
            if i < len(A)-1 and A[i+1][j] >= 0 and (i+1, j) not in visited:
                visited.add((i+1, j))
                queue.append((next_val, i+1, j))
            if j > 0 and A[i][j-1] >= 0 and (i, j-1) not in visited:
                visited.add((i, j-1))
                queue.append((next_val, i, j-1))
            if j < len(A[0])-1 and A[i][j+1] >= 0 and (i, j+1) not in visited:
                visited.add((i, j+1))
                queue.append((next_val, i, j+1))

