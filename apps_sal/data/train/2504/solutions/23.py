class Solution:

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        return self.backtrack(arr, 0, 0, 0)

    def backtrack(self, arr, i, end, s):
        if end == len(arr):
            return s
        elif i > end:
            return self.backtrack(arr, 0, end + 1, s)
        elif len(arr[i:end + 1]) % 2 != 0:
            s += sum(arr[i:end + 1])
            return self.backtrack(arr, i + 1, end, s)
        else:
            return self.backtrack(arr, i + 1, end, s)
