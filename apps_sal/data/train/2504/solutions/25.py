class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        size = len(arr)

        for n in range(1, size + 1, 2):
            for i in range(size - (n - 1)):
                for k in range(i, i + n):
                    # total += sum(arr[i:i+n])
                    total += arr[k]

        return total
