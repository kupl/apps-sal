class Solution:
    def stoneGameII(self, A: List[int]) -> int:

        seen = {}

        def max_stones(sidx, m):
            if sidx == len(A):
                return 0
            if (sidx, m) not in seen:
                if len(A) - sidx <= 2 * m:
                    seen[sidx, m] = sum(A[sidx:])
                else:
                    res = 0
                    for x in range(1, 2 * m + 1):
                        new_sidx = sidx + x
                        res = max(res, sum(A[sidx:]) - max_stones(new_sidx, max(m, x)))
                    seen[sidx, m] = res
            return seen[sidx, m]

        return max_stones(0, 1)
