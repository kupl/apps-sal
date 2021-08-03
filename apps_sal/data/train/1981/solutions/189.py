class Solution:
    def maxSumRangeQuery(self, nums, requests) -> int:
        chafen = [0] * (len(nums) + 1)
        for req in requests:
            chafen[req[0]] += 1
            chafen[req[1] + 1] -= 1
        chafen = chafen[:-1]
        sum_count = []
        lastsum = 0
        for idx, cha in enumerate(chafen):
            lastsum += cha
            sum_count.append(lastsum)
        sum_count = sorted(sum_count)
        nums = sorted(nums)
        res = 0
        for idx in range(len(nums)):
            res += sum_count[idx] * nums[idx]
            res %= 1e9 + 7
        return int(res)
