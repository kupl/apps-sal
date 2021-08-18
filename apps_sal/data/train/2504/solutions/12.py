class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ret = 0
        for i in range(len(arr)):
            ret += arr[i] * ceil((len(arr) - i) * (i + 1) / 2)
        return ret
