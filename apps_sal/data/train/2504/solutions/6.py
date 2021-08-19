class Solution:

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        l = len(arr)
        sumtotal = 0
        for i in range(1, l + 1, 2):
            for j in range(1, l + 1):
                if j + i - 1 < l + 1:
                    sumtotal += sum(arr[j - 1:j + i - 1])
        return sumtotal
