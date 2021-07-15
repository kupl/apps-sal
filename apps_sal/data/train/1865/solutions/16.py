class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == \"T\":
                    target = (r, c)
                if grid[r][c] == \"B\":
                    start_box = (r, c)
                if grid[r][c] == \"S\":
                    start_person = (r, c)
                    
        def heuristic(box):
            # return abs(target[0] - box[0]) + abs(target[1] - box[1])
            return 0;
        
        def out_bounds(location):  # return whether the location is in the grid and not a wall
            r, c = location
            if r < 0 or r >= rows:
                return True
            if c < 0 or c >= cols:
                return True
            return grid[r][c] == \"#\"
                        
        heap = [[heuristic(start_box), 0, start_person, start_box]]
        visited = set()
        
        while heap:
            _, moves, person, box = heapq.heappop(heap)
            if box == target:
                return moves
            if (person, box) in visited: # do not visit same state again
                continue
            visited.add((person, box))
            
            for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                new_person = (person[0] + dr, person[1] + dc)
                if out_bounds(new_person):
                    continue
                    
                if new_person == box:
                    new_box = (box[0] + dr, box[1] + dc)
                    if out_bounds(new_box):
                        continue
                    heapq.heappush(heap, [heuristic(new_box) + moves + 1, moves + 1, new_person, new_box])
                else:
                    heapq.heappush(heap, [heuristic(box) + moves, moves, new_person, box]) # box remains same
        
        return -1
