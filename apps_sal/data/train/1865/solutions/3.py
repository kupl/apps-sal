class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == 'T':
                    target_row, target_col = r, c
                    grid[r][c] = '.'
                elif grid[r][c] in 'B':
                    box_row, box_col = r, c
                    grid[r][c] = '.'
                elif grid[r][c] in 'S':
                    src_row, src_col = r, c
                    grid[r][c] = '.'
        def traversal(player_row, player_col, box_row, box_col, visited):
            if not (0 <= player_row < num_rows and 0 <= player_col < num_cols):
                return visited
            if grid[player_row][player_col] != '.' or (player_row, player_col) in visited:
                return visited
            visited.add((player_row, player_col))
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_player_row = player_row + i
                new_player_col = player_col + j
                if new_player_row != box_row or new_player_col != box_col:
                    traversal(new_player_row, new_player_col, box_row, box_col, visited)
            return visited
        queue = deque([(src_row, src_col, box_row, box_col, 0)])
        visited = {(src_row, src_col, box_row, box_col)}
        while queue:
            curr_row, curr_col, box_row, box_col, num_pushs = queue.popleft()
            reachable = traversal(curr_row, curr_col, box_row, box_col, set())
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_box_row = box_row+i
                new_box_col = box_col+j
                if not (0 <= new_box_row < num_rows and 0 <= new_box_col < num_cols):
                    continue
                if grid[new_box_row][new_box_col] != '.':
                    continue
                if (box_row - i, box_col - j) in reachable and (box_row, box_col, new_box_row, new_box_col) not in visited:
                    visited.add((box_row, box_col, new_box_row, new_box_col))
                    if new_box_row == target_row and new_box_col == target_col:
                        return num_pushs + 1
                    queue.append((box_row, box_col, new_box_row, new_box_col, num_pushs + 1))
        return -1

