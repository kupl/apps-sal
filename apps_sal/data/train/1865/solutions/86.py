class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
                
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    man = (i, j)
                elif grid[i][j] == 'B':
                    box = (i, j)
                elif grid[i][j] == 'T':
                    target = (i, j)
        
        def validPos(loc):
            i, j = loc
            return (m > i >= 0 <= j < n) and grid[i][j] != '#'
        
        def heuristic(box):
            return abs(target[0] - box[0]) + abs(target[1] - box[1])
        
        heap = [(heuristic(box), 0, man, box)]
        seen = set()
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while heap:
            _, steps, man, box = heapq.heappop(heap)
            if box == target:
                return steps
            if (man, box) in seen:
                continue
            seen.add((man, box))
            for r, c in dirs:
                new_man = man[0] + r, man[1] + c
                if not validPos(new_man):
                    continue
                if new_man == box:
                    new_box = box[0] + r, box[1] + c
                    if not validPos(new_box):
                         continue
                    heapq.heappush(heap, (heuristic(new_box) + steps + 1, steps + 1, new_man, new_box))
                else:
                    heapq.heappush(heap, (heuristic(box) + steps, steps, new_man, box))
                    
        return -1
