class Solution:

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        for i in range(1, len(arr) + 1, 2):
            for j in range(len(arr) + 1 - i):
                for k in range(i):
                    ans += arr[j + k]
        return ans
