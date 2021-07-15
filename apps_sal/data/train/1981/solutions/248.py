class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        count = [0] * (n + 1)
        for i, j in requests:
            count[i] += 1
            count[j + 1] -= 1
        for i in range(1, n + 1):
            count[i] += count[i - 1]
        # print(count)
        count.sort(reverse = True)
        res = 0
        nums.sort()
        for i in range(n):
            if count[i] == 0:
                break
            res += count[i] * nums.pop()
        return res % (10 ** 9+7)
