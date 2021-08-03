class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:

        total = 0
        length = 1

        while length <= len(arr):
            for i in range(len(arr) - length + 1):
                total += sum(arr[i:i + length])
            length += 2

        return total
