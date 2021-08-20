class Solution:

    def maxSumRangeQuery(self, nums, requests) -> int:
        mod_num = 10 ** 9 + 7
        n = len(nums)
        freq_arr = [0 for _ in range(n + 1)]
        for (i, j) in requests:
            freq_arr[i] += 1
            freq_arr[j + 1] -= 1
        for i in range(1, n + 1):
            freq_arr[i] += freq_arr[i - 1]
        result = sum([num * freq % mod_num for (num, freq) in zip(sorted(nums), sorted(freq_arr[:n]))]) % mod_num
        return result
