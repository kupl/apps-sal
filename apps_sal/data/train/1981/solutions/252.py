from collections import Counter


class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        start = Counter([r[0] for r in requests])
        end = Counter([r[1] for r in requests])
        running_sum = 0
        requests_per_num = []
        for (i, n) in enumerate(nums):
            running_sum += start[i]
            running_sum -= end[i - 1]
            requests_per_num.append(running_sum)
        requests_per_num.sort(reverse=True)
        nums_copy = [n for n in nums]
        nums_copy.sort(reverse=True)
        max_sum = 0
        for (n, r) in zip(nums_copy, requests_per_num):
            max_sum += n * r
        return max_sum % (10 ** 9 + 7)
