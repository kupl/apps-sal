class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        times_requested = [0 for i in range(len(nums))]

        for request in requests:
            start, end = request[0], request[1]
            times_requested[end] += 1
            if start - 1 >= 0:
                times_requested[start - 1] -= 1

        curr_sum = 0
        for i in range(len(times_requested) - 1, -1, -1):
            curr_sum += times_requested[i]
            times_requested[i] = curr_sum

        times_requested.sort()
        nums.sort()
        ans = 0
        for i in range(len(nums) - 1, -1, -1):
            ans += times_requested[i] * nums[i]
            ans = ans % (10 ** 9 + 7)
        return ans
