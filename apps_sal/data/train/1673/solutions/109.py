class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        if not arr:
            return 0

        R = C = len(arr)

        for r in range(1, R):
            for c in range(0, C):

                m = float('inf')
                for i in range(C):
                    if i != c:
                        m = min(m, arr[r - 1][i])

                arr[r][c] += m
            # print(arr[r], m)

        return min(arr[-1])
