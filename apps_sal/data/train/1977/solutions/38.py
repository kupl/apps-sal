class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        seen =  set([])
        stack =  []
        closed = True
        count = 0
        
        rows = len(grid)
        cols =  len(grid[0])
        
        for row in range(rows): 
            for col in range(cols): 
                if not grid[row][col] and (row,col) not in seen:
                    closed = True
                    stack.append((row,col))
                    while len(stack) > 0: 
                        node = stack.pop() 
                        if node in seen: continue
                        if node[0]-1>=0 and not grid[node[0]-1][node[1]] and (node[0]-1,node[1]) not in seen:  
                            stack.append((node[0]-1,node[1]))
                        elif node[0]-1 < 0: 
                            closed = False
                        if node[1]-1>=0 and not grid[node[0]][node[1]-1] and (node[0],node[1]-1) not in seen:
                            stack.append((node[0],node[1]-1))
                        elif node[1]-1 < 0:
                            closed = False
                        if node[0]+1 < rows and not grid[node[0]+1][node[1]] and (node[0]+1,node[1]) not in seen:  
                            stack.append((node[0]+1,node[1]))
                        elif node[0]+1 >= rows:
                            closed = False
                        if node[1]+1 < cols and not grid[node[0]][node[1]+1] and (node[0],node[1]+1) not in seen:
                            stack.append((node[0],node[1]+1))
                        elif node[1]+1 >= cols:
                            closed = False
                        seen.add(node)
                    if closed: count += 1
 
        return count
