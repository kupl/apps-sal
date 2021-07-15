class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dq = collections.deque() # Front is left, back is right
        dq.append(((0,1),1,0,\"first move\")) # position of head, orientation, distance travelled
        seen = set()
        while len(dq) > 0:
            pos,orientation,dist,move = dq.popleft()
            # print(pos,orientation,dist,move,dq)
            i,j = pos
            if (pos,orientation) not in seen:
                seen.add((pos,orientation))
                if pos == (n-1,n-1):
                    if orientation == 1:
                        return dist
                    else:
                        pass
                else:
                    if orientation == 1:
                        if j < n - 1 and grid[i][j+1] == 0:
                            dq.append(((i,j+1),orientation,dist+1,\"go right\"))
                        if i < n - 1 and grid[i+1][j] == 0 and grid[i+1][j-1] == 0:
                            dq.append(((i+1,j),orientation,dist+1,\"go down\"))
                        if i < n - 1 and grid[i+1][j] == 0 and grid[i+1][j-1] == 0:
                            dq.append(((i+1,j-1),1-orientation,dist+1,\"rotate clockwise\"))
                    else:
                        if i < n - 1 and grid[i+1][j] == 0:
                            dq.append(((i+1,j),orientation,dist+1,\"go down\"))
                        if j < n - 1 and grid[i][j+1] == 0 and grid[i-1][j+1] == 0:
                            dq.append(((i,j+1),orientation,dist+1,\"go right\"))
                        if j < n - 1 and grid[i][j+1] == 0 and grid[i-1][j+1] == 0:
                            dq.append(((i-1,j+1),1-orientation,dist+1,\"rotate counterclockwise\"))
        return -1
