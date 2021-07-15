class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if not grid:
            return 0
        nr = len(grid)
        nc = len(grid[0])
        
        seen = set() # (r, c, remaining k)
        if grid[0][0] == 0:
            start = (0,0,k)
        elif grid[0][0] == 1:
            start = (0,0,k-1)
        
        seen.add(start)
        curr_level = [start]
        level = 0
        while curr_level:
            next_level = []
            for r, c, ob in curr_level:
                if r == nr-1 and c == nc-1:
                    return level
                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    new_r, new_c = r + dr, c + dc
                    if 0 <= new_r < nr and 0 <= new_c < nc:
                        if grid[new_r][new_c] == 1:
                            if ob == 0:
                                continue
                            new_item = (new_r, new_c, ob-1)
                            if new_item not in seen:
                                seen.add(new_item)
                                next_level.append(new_item)
                        else: # == 0
                            new_item = (new_r, new_c, ob)
                            if new_item not in seen:
                                seen.add(new_item)
                                next_level.append(new_item)
            curr_level = next_level
            level += 1
        return -1
        
        
        

