from functools import lru_cache


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:

        n = len(mat)
        m = len(mat[0])

        total = 0
        for i in range(n):
            for j in range(m):
                bound = m
                for k in range(i, n):
                    l = j
                    while l < bound:
                        if mat[k][l]:
                            total += 1
                            l += 1
                        else:
                            bound = l
        return total
