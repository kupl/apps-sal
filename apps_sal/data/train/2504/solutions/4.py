class Solution:

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        size = len(arr)
        for n in range(1, size + 1, 2):
            for i in range(size - (n - 1)):
                total += sum(arr[i:i + n])
        return total
