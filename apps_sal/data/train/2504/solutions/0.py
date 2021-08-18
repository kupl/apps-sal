class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:

        total = 0
        for i in range(len(arr)):
            totalisubarrays = (len(arr) - i) * (i + 1)
            if totalisubarrays % 2 == 1:
                totalisubarrays += 1
            oddisubarrays = totalisubarrays // 2
            total += arr[i] * oddisubarrays
        return total
