class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        ans = []

        for i in range(0, len(mat)):
            ans.append([])
            for j in range(0, len(mat[0])):
                rL = max(0, i - K)
                rR = min(len(mat) - 1, i + K)
                cL = max(0, j - K)
                cR = min(len(mat[0]) - 1, j + K)
                posVal = 0
                for rVal in range(rL, rR + 1):
                    for cVal in range(cL, cR + 1):
                        posVal += mat[rVal][cVal]
                ans[i].append(posVal)
        return ans
