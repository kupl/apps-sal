class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        reqs = [0] * (len(nums) + 1)
        for request in requests:
            reqs[request[0]] += 1
            reqs[request[1] + 1] -= 1
        prev = 0
        reqs.pop()
        for i in range(len(reqs)):
            reqs[i] += prev
            prev = reqs[i]
        nums.sort(reverse=True)
        reqs.sort(reverse=True)
        ret = 0
        M = pow(10, 9) + 7
        for i in range(len(nums)):
            ret = (ret + nums[i] * reqs[i]) % M
        return ret
