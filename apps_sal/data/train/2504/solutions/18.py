class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        i = 0
        j = 1
        while True:
            if i > len(arr) - 1:
                break
            if len(arr[i:j]) % 2 != 0:
                ans = ans + sum(arr[i:j])
            j += 1
            if j > len(arr):
                i += 1
                j = i + 1
        return ans
