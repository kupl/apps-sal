class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        cur_sum, prefix_sum = 0, [0] * (len(arr) + 1)
        ret = 0
        for i in range(1, len(arr) + 1):
            cur_sum += arr[i - 1]
            prefix_sum[i] = cur_sum
            for j in range(1, i + 1, 2):
                ret += prefix_sum[i] - prefix_sum[i - j]
        return ret
