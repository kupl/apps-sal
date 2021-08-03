class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        s = 0
        for i in range(n):
            for j in range(1, n + 1, 2):
                if i + j - 1 < n:
                    for x in range(j):
                        s += arr[x + i]
        return s
