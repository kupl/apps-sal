class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        result = 0
        n = len(mat)
        m = len(mat[0])
        consecutive_ones = [[0] * m for _ in range(n)]
        overall_ones = []
        for i in range(n):
            c = 0
            for j in range(m - 1, -1, -1):
                if mat[i][j] == 1:
                    c += 1
                    overall_ones.append((i, j))
                else:
                    c = 0
                consecutive_ones[i][j] = c
        while len(overall_ones) != 0:
            leftmost_point = overall_ones.pop()
            i = leftmost_point[0]
            j = leftmost_point[1]
            prev_row_width = float('inf')
            for row in range(i, n):
                curr_width = consecutive_ones[row][j]
                if curr_width == 0:
                    break
                result += min(prev_row_width, curr_width)
                prev_row_width = min(prev_row_width, curr_width)
        return result
