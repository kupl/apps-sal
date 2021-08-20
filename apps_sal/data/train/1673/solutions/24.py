class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:

        def second_smallest(nums):
            (s1, s2) = (float('inf'), float('inf'))
            for num in nums:
                if num <= s1:
                    (s1, s2) = (num, s1)
                elif num < s2:
                    s2 = num
            return s2
        n = len(arr)
        for i in range(1, n):
            for j in range(n):
                prevmin = min(arr[i - 1])
                prevmin2 = second_smallest(arr[i - 1])
                arr[i][j] += prevmin if prevmin != arr[i - 1][j] else prevmin2
        return min(arr[n - 1])
