class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        
        island_one = set()

        def dfs(r,c):
            if (r,c) in island_one:
                return 
            island_one.add((r,c))

            for r1, c1 in {(r+1,c), (r, c+1), (r-1,c), (r,c-1)}: 
                        if 0 <= r1 < len(A) and 0 <= c1 < len(A[0]) and (r1,c1) not in island_one and A[r1][c1] == 1:
                            dfs(r1, c1)

        f = False
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    dfs(i,j)
                    f = True
                    break
            if f: break


        def bfs():
            q = collections.deque([(r,c,0) for r,c in list(island_one)])
            seen = set()
            while q:
                r,c,level = q.popleft()

                if A[r][c] == 1 and (r,c) not in island_one:
                    return level-1

                for r1, c1 in {(r+1,c), (r, c+1), (r-1,c), (r,c-1)}: 
                        if 0 <= r1 < len(A) and 0 <= c1 < len(A[0]) and A[r1][c1] not in island_one and (r1,c1) not in seen:
                            q.append((r1,c1,level+1))
                            seen.add((r1,c1))
        return bfs()
                        
                        
            
            
    
    
    
        

