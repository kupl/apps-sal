class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        cnt = [0] * (len(nums) + 2)
        for a, b in requests:
            cnt[a] += 1
            cnt[b + 1] -= 1
        for i in range(len(nums)):
            cnt[i] += cnt[i - 1]
        cnt.sort(reverse=True)
        nums.sort(reverse=True)
        return sum(a * b for a, b in zip(cnt, nums)) % (10 ** 9 + 7)
