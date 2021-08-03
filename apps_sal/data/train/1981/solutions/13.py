class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        a = [0 for i in range(len(nums) + 1)]
        for i in requests:
            a[i[0]] += 1
            a[i[1] + 1] -= 1

        for i in range(1, len(a)):
            a[i] = a[i] + a[i - 1]

        a.pop(-1)

        nums = sorted(nums, reverse=True)

        pair = [[0, number, index] for index, number in enumerate(a)]
        pair = sorted(pair, key=lambda word: (-word[1]))

        for i in range(len(nums)):
            pair[i][0] = nums[i]

        maxSum = 0

        for i in pair:
            maxSum += i[0] * i[1]

        return maxSum % ((10 ** 9) + 7)
