class Solution:
    def maxSumRangeQuery(self, nums, requests) -> int:
        \"\"\"
        Given an array of integers (nums) and an array of range
        requests (requests), each request containing the start
        and end indexes of a range within nums, this program
        determines the maximum sum over requests for all permutations
        of nums.

        :param nums: array of integers
        :type nums: list[int]
        :param requests: array of range requests, each containing
                         the start and end indexes of a range of
                         indexes within nums
        :type requests: list[list[int]]
        :return: maximum sum over the range requests (requests)
        :rtype: int
        \"\"\"

        \"\"\"
        Initialize length of nums array (len_nums)
        \"\"\"
        len_nums = len(nums)

        \"\"\"
        Determine the frequency for each index within nums
        \"\"\"
        frequencies = [0] * (len_nums + 1)
        for start, end in requests:
            frequencies[start] += 1
            frequencies[end + 1] -= 1
        for k in range(1, len_nums):
            frequencies[k] += frequencies[k - 1]

        \"\"\"
        Determine the maximum range sum (max_sum).
        \"\"\"
        frequencies.sort(reverse=True)
        nums.sort(reverse=True)
        max_sum = 0
        for num, frequency in zip(nums, frequencies):
            max_sum += num * frequency
        return max_sum % (10**9 + 7)
