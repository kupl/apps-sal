class Solution:
    # https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/discuss/854206/JavaC%2B%2BPython-Sweep-Line
    # https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/discuss/854149/C%2B%2BJava-O(n-log-n)
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse = True)
        n = len(nums)
        counter = [0 for _ in range(n + 1)]
        for i, j in requests:
            counter[i] += 1
            counter[j + 1] -= 1
        for i in range(1, n + 1):
            counter[i] += counter[i - 1]
        counter.sort(reverse = True)
        res = 0
        for i in range(n):
            res += counter[i] * nums[i]
        return res % (10 ** 9 + 7)
