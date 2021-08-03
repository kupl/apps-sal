class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        index_count = [0] * (len(nums) + 1)
        for request in requests:
            index_count[request[0]] += 1
            index_count[request[1] + 1] -= 1

        for i in range(1, len(index_count)):
            index_count[i] += index_count[i - 1]
        nums.sort(reverse=True)
        index_count.sort(reverse=True)

        res = sum(i * v for i, v in zip(nums, index_count))
        return res % (10**9 + 7)
