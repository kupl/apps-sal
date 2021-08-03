from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        dq = deque()
        dq.append((0, 0, k, 0))
        visited = set()
        visited.add((0, 0, k))

        while dq:
            cur = dq.popleft()
            row = cur[0]
            col = cur[1]
            elm = cur[2]
            pth = cur[3]
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return pth

            if col < len(grid[0]) - 1:
                if grid[row][col + 1] == 1:
                    if elm > 0 and (row, col + 1, elm - 1) not in visited:
                        dq.append((row, col + 1, elm - 1, pth + 1))
                        visited.add((row, col + 1, elm - 1))
                elif (row, col + 1, elm) not in visited:
                    dq.append((row, col + 1, elm, pth + 1))
                    visited.add((row, col + 1, elm))

            if row < len(grid) - 1:
                if grid[row + 1][col] == 1:
                    if elm > 0 and (row + 1, col, elm - 1) not in visited:
                        dq.append((row + 1, col, elm - 1, pth + 1))
                        visited.add((row + 1, col, elm - 1))
                elif (row + 1, col, elm) not in visited:
                    dq.append((row + 1, col, elm, pth + 1))
                    visited.add((row + 1, col, elm))

            if row > 0:
                if grid[row - 1][col] == 1:
                    if elm > 0 and (row - 1, col, elm - 1) not in visited:
                        dq.append((row - 1, col, elm - 1, pth + 1))
                        visited.add((row - 1, col, elm - 1, pth + 1))
                elif (row - 1, col, elm) not in visited:
                    dq.append((row - 1, col, elm, pth + 1))
                    visited.add((row - 1, col, elm))

            if col > 0:
                if grid[row][col - 1] == 1:
                    if elm > 0 and (row, col - 1, elm - 1) not in visited:
                        dq.append((row, col - 1, elm - 1, pth + 1))
                        visited.add((row, col - 1, elm - 1))
                    elif (row, col - 1, elm) not in visited:
                        dq.append((row, col - 1, elm, pth + 1))
                        visited.add((row, col - 1, elm))
        return -1
