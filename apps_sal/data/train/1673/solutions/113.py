class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        import math
        n = len(arr)
        if n == 0:
            return 0
        k = len(arr[0])
        for house in range(1, n):
            for color in range(k):
                best = math.inf
                for prev_color in range(k):
                    if color == prev_color:
                        continue
                    best = min(best, arr[house - 1][prev_color])
                arr[house][color] += best
        return min(arr[-1])
