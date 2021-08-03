class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        #BFS. 终止条件为箱子到达目标点，或者这条路走过且有更短的走法.
        n = len(grid)
        m = len(grid[0])
        
        player = None
        box = None
        dest = None
        for i in range(n):
            for j in range(m):
                if grid[i][j] == \"B\":
                    box = (i,j)
                    grid[i][j] = \".\"
                elif grid[i][j] == \"S\":
                    player = (i,j)
                    grid[i][j] = \".\"
                elif grid[i][j] == \"T\":
                    dest = (i, j)
                    grid[i][j] = \".\"
                if player != None and box != None and dest != None:
                    break
                    
        def can_move(r, c, n, m, d, br, bc, cost):
            if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] == '#':
                return False
            if (br,bc) == (r,c):
                nbr, nbc = r+d[0], c+d[1]
                br, bc = nbr, nbc
                if nbr < 0 or nbr >= n or nbc < 0 or nbc >= m or grid[nbr][nbc] == '#':
                    return False
                cost += 1
            if visited[(r,c,br,bc)] <= cost:
                return False
                
            return (br,bc, cost)
        
        visited = collections.defaultdict(lambda: float(\"inf\"))
        q = [(player[0], player[1], box[0], box[1],0)]
        res = float(\"inf\")
        while len(q)>0:
            next_q = []
            for r,c, br, bc, cost in q:
                # print(r,c, br, bc, cost, pushes)
                #看看四个方向能不能移动, 有没有箱子，有没有墙，是否走过
                dir = [(-1,0),(1,0),(0,1),(0,-1)]
                for d in dir:
                    # print(\"d\", d)
                    nr, nc = r+d[0], c+d[1]
                    move_res = can_move(nr, nc, n, m, d, br, bc, cost)
                    if move_res != False:
                        nbr, nbc, new_cost = move_res
                        visited[(nr,nc,br,bc)] = new_cost
                        #判断是否到达目的地
                        if (nbr,nbc) == dest:
                            res = min(res, new_cost)
                        else:
                            #没有到达目标才需要继续遍历
                            if (nbr,nbc) == (br,bc):
                                next_q.append((nr,nc,nbr,nbc,new_cost))
                            else:
                                next_q.append((nr,nc,nbr,nbc,new_cost))
                    else:
                        # print(\"False\", nr,nc, br, bc, cost)
                        pass
                            
            q = next_q
            
        # print(visited)
        return res if res != float(\"inf\") else -1
