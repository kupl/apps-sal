class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        ## from https://leetcode-cn.com/problems/minimum-moves-to-move-a-box-to-their-target-location/solution/bfsbfs-by-haitao-yu/
        ## 双 BFS
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        M = len(grid)
        N = len(grid[0])
    
        def find_target(target):
            row,col = None, None
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == target:
                        row, col = i,j
                        break
            return row, col
        
        def check_pos_valid(i,j):
            if i >=0 and i < M and j >= 0 and j < N and grid[i][j] in [\"T\",\".\"]:
                return True
            else :
                return False
    
        def player_bfs(player_x,player_y, behind_box_x,behind_box_y):
            
            queue = [(player_x,player_y)]
            visited = set()
    
            while len(queue) !=0:
                player_x,player_y = queue.pop(0)
                visited.add((player_x,player_y))
                
                if (player_x,player_y) == (behind_box_x,behind_box_y):
                    return True
                
                for dx,dy in directions:
                    next_x = player_x + dx
                    next_y = player_y + dy
                    if check_pos_valid(next_x, next_y) and (next_x, next_y) not in visited:
                        queue.append( (next_x, next_y) )
                        visited.add( (next_x, next_y) )
            return False
    
    
    
        box_x,box_y = find_target(\"B\")
        player_x,player_y = find_target(\"S\")
        end_x, end_y = find_target(\"T\")
        init_state = (box_x,box_y, player_x,player_y,0)
        queue = [init_state]
        visited = set()
        visited.add((box_x,box_y, player_x,player_y))
    
        ## 清除 B 和 S
        grid[box_x][box_y] = \".\"
        grid[player_x][player_y] = \".\"
    
    
        # ## BFS #1
        while len(queue) !=0 :
            # print(queue)
            box_x,box_y, player_x,player_y, step  = queue.pop(0)
            
            ## 检查箱子状态
            if (box_x, box_y) == (end_x, end_y):
                return step
            
            ## 更新箱子的位置
            grid[box_x][box_y] = \"B\"  ## B 是可以挡路的，导致 player 无法绕到箱子后。在对 player bfs 时需要考虑，因此置之为 B
            for dx,dy in directions:
                ## 箱子的下一个可能的位置
                box_next_x = box_x + dx
                box_next_y = box_y + dy
                if check_pos_valid(box_next_x, box_next_y):
                    ## 如果箱子的下一个可能位置合法，则检查当前箱子的后方位置是否合法（合法的话，箱子才可能移动到下一个位置）
                    behind_box_x = box_x - dx
                    behind_box_y = box_y - dy
                    if check_pos_valid(behind_box_x, behind_box_y):
                        ## 后方位置也合法，检查 player 是否能走到该位置(可以使用 bfs)
                        if player_bfs(player_x,player_y, behind_box_x,behind_box_y):
                            ## 如果可以走到，且当前位置未访问，则加入队列
                            next_state = (box_next_x, box_next_y, behind_box_x, behind_box_y, step+1)
                            if (box_next_x, box_next_y, behind_box_x, behind_box_y) not in visited:
                                queue.append(next_state)
                                visited.add((box_next_x, box_next_y, behind_box_x, behind_box_y))
            grid[box_x][box_y] = \".\"
        return -1   
