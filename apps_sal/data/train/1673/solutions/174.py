class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        if not arr:
            return 0

        prev = arr[0]
        curr = [0 for i in range(len(prev))]

        for cost in arr[1:]:
            for i in range(len(cost)):
                tmp = prev[:i] + prev[i + 1:]
                curr[i] = min(tmp) + cost[i]
            prev[:] = curr[:]

        return min(prev)
