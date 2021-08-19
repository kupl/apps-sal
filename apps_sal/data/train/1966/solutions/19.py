class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        M = len(mat)
        N = len(mat[0])
        res = 0
        for top in range(M):
            for left in range(N):
                bound = N
                for bottom in range(top, M):
                    right = left
                    while right < bound:
                        if mat[bottom][right] == 1:
                            res += 1
                            right += 1
                        else:
                            bound = right
                            break
        return res
