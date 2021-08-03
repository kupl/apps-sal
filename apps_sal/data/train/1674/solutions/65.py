class Solution:
    def stoneGameII(self, A: List[int]) -> int:

        # my solution ... 96 ms ... 51 % ... 14.9 MB ... 25 %
        #  time: O()
        # space: O()

        seen = {}

        def max_stones(sidx, m):  # 返回面对 A[sidx:] 时，直至游戏结束，所能取到的最多石头
            if sidx == len(A):
                return 0
            if (sidx, m) not in seen:
                if len(A) - sidx <= 2 * m:
                    seen[sidx, m] = endsum[sidx]  # sum(A[sidx:])
                else:
                    res = 0
                    for x in range(1, 2 * m + 1):
                        new_sidx = sidx + x
                        res = max(res, endsum[sidx] - max_stones(new_sidx, max(m, x)))
                    seen[sidx, m] = res
            return seen[sidx, m]

        endsum = [A[-1]] * len(A)
        for j in range(len(A) - 2, -1, -1):
            endsum[j] = A[j] + endsum[j + 1]
        return max_stones(0, 1)
