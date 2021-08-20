class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        req = [0] * (len(nums) + 1)
        for r in requests:
            req[r[0]] += 1
            req[r[1] + 1] -= 1
        for i in range(1, len(req)):
            req[i] += req[i - 1]
        req = sorted(req, reverse=True)
        nums = sorted(nums, reverse=True)
        answer = 0
        for i in range(len(nums)):
            if req[i] == 0 or nums[i] == 0:
                return answer % 1000000007
            answer += req[i] * nums[i]
        return answer % 1000000007
