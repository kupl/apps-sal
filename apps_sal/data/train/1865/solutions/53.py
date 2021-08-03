import heapq


class Solution:
    def est_distance(self, grid, target_posi, box_posi, move):
        return move + abs(target_posi[0] - box_posi[0]) + abs(target_posi[1] - box_posi[1])

    def isvalid_posi(self, grid, m, n, posi):
        i, j = posi
        if i < 0 or i >= m or j < 0 or j >= n:
            return False
        return grid[i][j] != '#'

    def minPushBox(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'B':
                    box_posi = (i, j)
                if grid[i][j] == 'T':
                    target_posi = (i, j)
                if grid[i][j] == 'S':
                    start_posi = (i, j)

        seen = set()
        seen.add((box_posi, start_posi))

        init_dist = self.est_distance(grid, target_posi, box_posi, 0)
        heap = [(init_dist, 0, box_posi, start_posi)]

        while heap:
            dist, move, current_box, current_human = heapq.heappop(heap)
            if current_box == target_posi:
                return move
            for row_move, col_move in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                new_human = (current_human[0] + row_move, current_human[1] + col_move)
                if not self.isvalid_posi(grid, m, n, new_human):
                    continue
                if (current_box, new_human) not in seen:
                    if new_human == current_box:
                        new_box = (current_box[0] + row_move, current_box[1] + col_move)
                        if self.isvalid_posi(grid, m, n, new_box):
                            seen.add((new_box, new_human))
                            new_dist = self.est_distance(grid, target_posi, new_box, move + 1)
                            heapq.heappush(heap, (new_dist, move + 1, new_box, new_human))
                    else:
                        seen.add((current_box, new_human))
                        new_dist = self.est_distance(grid, target_posi, current_box, move)
                        heapq.heappush(heap, (new_dist, move, current_box, new_human))

        return -1
