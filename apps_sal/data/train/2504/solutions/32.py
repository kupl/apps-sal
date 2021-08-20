class Solution:

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        N = len(arr)
        sumv = (N + 1) * [0]
        for i in range(N):
            sumv[i + 1] = sumv[i] + arr[i]
        ans = 0
        for i in range(1, N + 1):
            ans += sumv[i] * ((i + 1) // 2 - (N - i + 1) // 2)
        return ans
