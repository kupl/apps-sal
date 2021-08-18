class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        acc, his = 0, [0] * len(mat[0])
        for i, row in enumerate(mat):
            for j, v in enumerate(row):
                his[j] = his[j] + 1 if v else 0
                cap = float('inf')
                for height in his[:j + 1][::-1]:
                    cap = min(cap, height)
                    if not cap:
                        break
                    acc += cap
        return acc
