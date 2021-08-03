class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = sum(arr)
        for i in range(0, len(arr)):
            count = 2
            while (i + count) < len(arr):
                for j in range(i, count + i + 1):
                    res += arr[j]
                count += 2
        return res
