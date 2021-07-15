class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        player = box = target = None
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == \"B\":
                    box = (i, j)
                elif grid[i][j] == \"S\":
                    player = (i, j)
                elif grid[i][j] == \"T\":
                    target = (i, j)
        
        def is_valid(pos):
            r, c = pos
            if 0 <= r < rows and 0 <= c < cols:
                return grid[r][c] != \"#\"
            return False
        
        def get_distance(box):
            return abs(target[0] - box[0]) + abs(target[1] - box[1])
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        heap = [(get_distance(box), 0, player, box)]
        visited = set()
        
        while heap:
            distance, move, player, box = heapq.heappop(heap)
            if box == target:
                return move
            if (player, box) in visited:
                continue
            visited.add((player, box))
            for d in directions:
                next_player = (player[0] + d[0], player[1] + d[1])
                if not is_valid(next_player):
                    continue
                if box == next_player:
                    next_box = (box[0] + d[0], box[1] + d[1])
                    if not is_valid(next_box):
                        continue
                    heapq.heappush(heap, (get_distance(next_box) + move + 1, move + 1, next_player, next_box))
                else:
                    heapq.heappush(heap, (distance, move, next_player, box))
        return -1
