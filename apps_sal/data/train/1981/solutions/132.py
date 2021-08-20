class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        request_counts = [0] * (len(nums) + 1)
        for (start, end) in requests:
            request_counts[start] += 1
            request_counts[end + 1] -= 1
        cur_count = 0
        for i in range(len(nums) + 1):
            cur_count += request_counts[i]
            request_counts[i] = cur_count
        nums.sort(reverse=True)
        sorted_idxs = sorted(range(len(nums) + 1), key=lambda i: request_counts[i], reverse=True)
        ans = 0
        for (idx, num) in zip(sorted_idxs, nums):
            ans += num * request_counts[idx]
        return ans % int(1000000000.0 + 7)
