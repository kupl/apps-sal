class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        
        def player_moves(box_i, box_j, player_i, player_j):
            res=[]
            if player_i > 0 and grid[player_i-1][player_j] != '#' and (player_i-1, player_j) != (box_i, box_j):
                res.append((player_i-1, player_j))
            if player_i < len(grid)-1 and grid[player_i+1][player_j] != '#' and (player_i+1, player_j) != (box_i, box_j):
                res.append((player_i+1, player_j))
            if player_j > 0 and grid[player_i][player_j-1] != '#' and (player_i, player_j-1) != (box_i, box_j):
                res.append((player_i, player_j-1))    
            if player_j < len(grid[0])-1 and grid[player_i][player_j+1] != '#' and (player_i, player_j+1) != (box_i, box_j):
                res.append((player_i, player_j+1))
            return res
                    
        def can_player_access_cell(cell_i, cell_j, box_i, box_j, player_i, player_j):
            if grid[cell_i][cell_j]=='#':
                return False
            q=deque()
            visited=set()
            q.append((player_i, player_j))
            visited.add((player_i, player_j))
            while q:
                size=len(q)
                for i in range(size):
                    pop=q.popleft()
                    if pop==(cell_i,cell_j):
                        return True
                    for nex in player_moves(box_i, box_j, pop[0], pop[1]):
                        if nex not in visited:
                            q.append(nex)
                            visited.add(nex)
            return False 
            
        def box_moves(state):
            res=set()
            print(('state', state))
            box_i, box_j, player_i, player_j = state[0], state[1], state[2], state[3]
            print(('box_i',box_i))
            # first check box's four neighbor if empty floor cell, and accessible to player, the cell of opposite direction should also be empty# moves, update box location, mark B, update player location
            if box_i>0 and can_player_access_cell(box_i-1, box_j, box_i, box_j, player_i, player_j) and box_i+1<len(grid) and grid[box_i+1][box_j]!='#':  # push down, player replace box location
                res.add((box_i+1, box_j, box_i, box_j))
            if box_i<len(grid)-1 and can_player_access_cell(box_i+1, box_j, box_i, box_j, player_i, player_j) and box_i-1>=0 and grid[box_i-1][box_j]!='#':   # push up
                res.add((box_i-1, box_j, box_i, box_j))
            if box_j>0 and can_player_access_cell(box_i, box_j-1, box_i, box_j, player_i, player_j) and box_j+1<len(grid[0]) and grid[box_i][box_j+1]!='#':  # push right
                res.add((box_i, box_j+1, box_i, box_j))
            if box_j<len(grid[0])-1 and can_player_access_cell(box_i, box_j+1, box_i, box_j, player_i, player_j) and box_j-1>=0 and grid[box_i][box_j-1]!='#':  # push left
                res.add((box_i, box_j-1, box_i, box_j))
            print(('res', res))
            return res
            
            
        def start_state():
            box_i, box_j, player_i, player_j = -1, -1, -1, -1
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]=='B':
                        box_i, box_j = i, j
                    elif grid[i][j]=='S':
                        player_i, player_j = i, j
            return (box_i, box_j, player_i, player_j)
                
        q=deque()
        visited=set()
        start=start_state()
        q.append(start)
        visited.add(start)
        moves=-1
        while q:
            size=len(q)
            print(size)
            print(q)
            moves +=1
            
            for i in range(size):
                pop=q.popleft()
                print(('pop', pop))
                if grid[pop[0]][pop[1]]=='T':
                    return moves
                    
                for nx in box_moves(pop):
                    print(('nx',nx))
                    
                    if nx not in visited:
                        q.append(nx)
                        visited.add(nx)
                    
        return -1
        
                
                
                
                

