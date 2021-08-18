class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])

        def one_d_sum(h):
            ans = 0
            length = 0
            for i in range(len(h)):
                if h[i] == 1:
                    length += 1
                else:
                    length = 0
                ans += length
            return ans

        ans = 0
        for top_row in range(rows):
            h = [1] * cols
            for bottom_row in range(top_row, rows):
                for k in range(cols):
                    h[k] = h[k] & mat[bottom_row][k]
                ans += one_d_sum(h)
        return ans
