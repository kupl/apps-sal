class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == \"T\":
                    target = (i, j)
                if grid[i][j] == \"B\":
                    box = (i, j)
                if grid[i][j] == \"S\":
                    person = (i, j)
                    
        def valid(x, y):
            return 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y] != \"#\"
        
        def check(curr, dest, box):
            queue = deque([curr])
            v = set()
            while queue:
                pos = queue.popleft()
                if pos == dest:
                    return True
                new_pos = [(1,0),(-1,0),(0,1),(0,-1)]
                for x, y in new_pos:
                    nx, ny = pos[0]+x, pos[1]+y
                    if valid(nx, ny) and (nx, ny) not in v and (nx, ny) != box:
                        v.add((nx, ny))
                        queue.append((nx, ny))
                        
            return False
        
        
        
        queue = deque([(0,box,person)])
        visited = {box+person}
        while queue:
            dist, box, person = queue.popleft()
            if box == target:
                return dist
            
            #these are the new possible coordinates/indices box can be placed in (up, down, right, left).
            # b_coord = [(box[0]+1,box[1]),(box[0]-1,box[1]),(box[0],box[1]+1),(box[0],box[1]-1)]
            b_coord = [(1,0),(-1,0),(0,1),(0,-1)]
            #these are the corresponding coordinates the person has to be in to push .. the box into the new coordinates
            # p_coord = [(box[0]-1,box[1]),(box[0]+1,box[1]),(box[0],box[1]-1),(box[0],box[1]+1)]
            p_coord = [(-1,0),(1,0),(0,-1),(0,1)]
            
            for new_box,new_person in zip(b_coord,p_coord):
                bx, by = box[0]+new_box[0], box[1]+new_box[1]
                px, py = box[0]+new_person[0], box[1]+new_person[1]
                
                if valid(bx, by) and box+new_box not in visited:
                    if valid(px, py) and check(person,(px, py),box):
                        visited.add((box+new_box))
                        queue.append((dist+1,(bx, by),box))
                        ###after shifting, the person's pos is old box's pos
        return -1
            
        
                    
                
        
