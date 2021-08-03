import heapq


class Solution:
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def shortestBridge(self, mat: List[List[int]]) -> int:
        row = None
        col = None
        found = False
        for i in range(len(mat)):
            if found:
                break
            for j in range(len(mat[i])):
                if mat[i][j]:
                    row = i
                    col = j
                    Solution.paint_one_island(mat, row, col, mat[row][col] + 1)
                    found = True
                    break
        target_dest = 1
        return Solution.minimum_expand(mat, row, col, target_dest)

    @staticmethod
    def mark_next(mat, row, col, val, target_dest):
        for i in range(len(Solution.directions)):
            new_row = row + Solution.directions[i][0]
            new_col = col + Solution.directions[i][1]
            if new_row < 0 or new_row >= len(mat) or new_col < 0 or new_col >= len(mat[0]):
                continue
            if mat[new_row][new_col] == target_dest:
                return True
            if not mat[new_row][new_col]:
                mat[new_row][new_col] = val + 1
        return False

    @staticmethod
    def minimum_expand(mat, row, col, target_dest):
        st_val = mat[row][col]
        for val in range(st_val, len(mat) * len(mat[0])):
            for row in range(len(mat)):
                for col in range(len(mat[row])):
                    is_reached = False
                    if mat[row][col] == val:
                        is_reached = Solution.mark_next(mat, row, col, val, target_dest)
                    if is_reached:
                        return val - st_val
        return -1

    @staticmethod
    def paint_one_island(mat, row, col, val):
        if row < 0 or row >= len(mat) or col < 0 or col >= len(mat[0]):
            return
        if mat[row][col] == val or not mat[row][col]:
            return
        mat[row][col] = val
        for i in range(len(Solution.directions)):
            Solution.paint_one_island(mat, row + Solution.directions[i][0], col + Solution.directions[i][1], val)
