class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        visited = {str(cells) : N}
        
        cycle = 0
        hascycle = False
        
        def get_next(cells) -> List[int]:
            '''return next cell'''
            tmp = [0] + [cells[i-1] ^ cells[i+1] ^ 1 for i in range(1,7)] + [0]
            return tmp
            
        
        while N > 0:
            visited[str(cells)] = N
            
            N -= 1
            cells = get_next(cells.copy())
            if str(cells) in visited:
                hascycle = True
                cycle = visited[str(cells)] - N 
                break
            
            
        if hascycle:
            N = N % cycle
            while N > 0:
                N -= 1
                cells = get_next(cells)
            
        return cells
