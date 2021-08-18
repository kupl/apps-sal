class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        row = len(mat)
        col = len(mat[0])
        for j in range(col):
            for i in range(1, row):
                mat[i][j] = mat[i - 1][j] + 1 if mat[i][j] == 1 else 0

        total = 0
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    continue
                cur = j
                delta = 0
                min_h = float('inf')
                while cur >= 0 and mat[i][cur] != 0:
                    cur_h_above = mat[i - 1][cur] if i - 1 >= 0 else 0
                    min_h = min(min_h, cur_h_above)
                    delta += (min_h + 1)
                    cur -= 1
                total += delta
        return total
