move_y = [1, 0, -1, 0]
move_x = [0, 1, 0, -1]

def langtons_ant(n):
    grid_size = 128
    grid = [[0 for i in range(grid_size)] for j in range(grid_size)]
    
    pos_x = int(grid_size/2)
    pos_y = int(grid_size/2)
    dir = 0
    
    cnt_blk = 0
    step_cnt = 0
    prev_cnt = []
    while step_cnt < n:
    
        # Check if reached steady state for step count > 10000 
        # and when remaining steps evenly divisible by cycle of 104
        if step_cnt > 1e4 and step_cnt % 104 == n%104:
            prev_cnt.append(cnt_blk)
            
            # If previous 5 black square counts have same difference, 
            # assume in cycle
            if len(prev_cnt) == 6:
                prev_cnt.pop(0)
                diff = prev_cnt[-1]-prev_cnt[-2]
                cycle_flg = True
                for i in range(len(prev_cnt)-2,0,-1):
                    if prev_cnt[i]-prev_cnt[i-1] != diff:
                        cycle_flg = False
                        break
                        
                # If in cycle, add up difference for however many steps 
                # left until n and then break out of walk simulation
                if cycle_flg:
                    cnt_blk += int(diff * (n-step_cnt)//104)
                    break
    
        # If on white square, flip to black and turn clockwise
        if grid[pos_x][pos_y] == 0:
            cnt_blk += 1
            grid[pos_x][pos_y] = 1
            dir = (dir+1)%4
        # If on black square, flip to white and turn counter-clockwise
        else:
            cnt_blk -= 1
            grid[pos_x][pos_y] = 0
            dir = (dir+4-1)%4
        
        # Advance one square based on new direction
        pos_x += move_x[dir]
        pos_y += move_y[dir]
        
        # Increment step counter
        step_cnt += 1
    return cnt_blk
