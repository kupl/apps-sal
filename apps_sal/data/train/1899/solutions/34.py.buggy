class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        
        R, C = len(A), len(A[0])
        visited =[[0 for i in range(len(A))] for j in range(len(A[0]))]
        boundary = set()
        island1 = set()
        dX = [0, 0, 1, -1]
        dY = [1, -1, 0 , 0]

        def dfs( visited, boundary, x, y):
            # print(x, y)
            if  0 <= x < C and 0 <= y < R and visited[x][y]==0:
                if A[x][y] == 1:
                    visited[x][y] = 1;
                    island1.add((x,y))
                    for dirX, dirY in zip(dX, dY):

                        dfs(visited, boundary, x+dirX, y + dirY)
                else:
                    boundary.add((x,y))
        \"\"\"
        step 1: use DFS to find the first island
        need to record island1 and boundary
        \"\"\"
        foundflag = 0;
        for i in range(C):
            for j in range(R):
                if A[i][j] == 1:
                    # print(\"found start\")
                    dfs(visited, boundary, i, j)
                    foundflag = 1;
                    break;
            if foundflag == 1:
                break;

        \"\"\"
        step 2: use BFS to find the shortest path
        need to record island1 and boundary
        \"\"\"
        queue = [x for x in boundary]
        bridge_len = 1;
        # visited =[[0 for i in range(len(A))] for j in range(len(A[0]))]
        
        while(len(queue) >0):
            
            for index in range(len(queue)):
                
                curX, curY = queue.pop(0);
                
                for dirX, dirY in zip(dX, dY):
                    
                    xtmp, ytmp = curX + dirX, curY + dirY;
                    
                    if  0 <= xtmp < C and 0 <= ytmp < R and visited[xtmp][ytmp] == 0:
                        
                        visited[xtmp][ytmp] = 1;
                        # if (xtmp,ytmp) not in island1:
                        if A[xtmp][ytmp] == 1:
                            return bridge_len;
                        else:
                            queue.append((xtmp, ytmp));
            bridge_len += 1;
