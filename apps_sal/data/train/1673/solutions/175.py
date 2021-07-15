class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        if not arr:
            return 0

        prev = arr[0]
        curr = [0 for i in range(len(prev))]

        for item in arr[1:]:
            for i in range(len(item)):
                curr[i] = min(prev[:i] + prev[i + 1:]) + item[i]
            prev[:] = curr[:]

        return min(prev)

