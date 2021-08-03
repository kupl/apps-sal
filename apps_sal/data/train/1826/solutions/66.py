class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        ans = []
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(sum([mat[r][c] for r in range(max(0, i - k), min(i + k + 1, m)) for c in range(max(0, j - k), min(n, j + k + 1))]))
            ans.append(temp)
        return ans
