class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if len(grid)==1 and len(grid[0]) == 1:
            return 0
        q = []
        visited = set((0,0,0))
        heapq.heappush(q,(0,0,(0,0)))
        while(len(q)>0):
            curr = heapq.heappop(q)
            if curr[2] == (len(grid)-1,len(grid[0])-1):
                return curr[0]
            else:
                for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    new_x = curr[2][0]+dx
                    new_y = curr[2][1]+dy
                    if new_x>=0 and new_x<len(grid) and new_y>=0 and new_y<len(grid[0]):
                        if grid[new_x][new_y] == 1:
                            if (curr[1]+1,new_x,new_y) not in visited and curr[1]+1<=k:
                                heapq.heappush(q,(curr[0]+1,curr[1]+1,(new_x,new_y)))
                                visited.add((curr[1]+1,new_x,new_y))
                        else:
                            if (curr[1],new_x,new_y) not in visited:
                                heapq.heappush(q,(curr[0]+1,curr[1],(new_x,new_y)))
                                visited.add((curr[1],new_x,new_y))
        return -1          
        
        # if len(grid)==1 and len(grid[0]) == 1:
        #     return 0
        # q = collections.deque()
        # visited = set((0,0,0))
        # q.append(((0,0),0))
        # level = 1
        # while(len(q)>0):
        #     length = len(q)
        #     for i in range(length):
        #         curr = q.popleft()
        #         for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        #             new_x = curr[0][0]+dx
        #             new_y = curr[0][1]+dy
        #             if new_x>=0 and new_x<len(grid) and new_y>=0 and new_y<len(grid[0]):
        #                 obs = curr[1]
        #                 if grid[new_x][new_y] == 1:
        #                     obs+=1
        #                 if (new_x,new_y,obs) not in visited and obs<=k:
        #                         visited.add((new_x,new_y, obs))
        #                         q.append(((new_x,new_y),obs))
        #                         if new_x == len(grid)-1 and new_y == len(grid[0])-1:
        #                             return level
        #     level+=1
        # return -1

