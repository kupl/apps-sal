class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat:
            return 0
        (rows, cols) = (len(mat), len(mat[0]))
        height = [0] * cols
        output = 0
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    height[c] = 0
                else:
                    height[c] += 1
                    v = height[c]
                    for i in range(c, -1, -1):
                        if height[i] == 0:
                            break
                        v = min(v, height[i])
                        output += v
        return output
        1 + 1 + 2 + 1 + 1 + 3 + 2 + 2
