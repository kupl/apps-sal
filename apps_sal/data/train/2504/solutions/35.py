class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        prefix = [0]*(n+1)
        for i in range(n): prefix[i] = prefix[i-1]+arr[i]
        ans = 0
        for s in range(1,n+1,2): 
            for i in range(n):
                if i+s > n: break
                ans += prefix[i+s-1] - prefix[i-1]
        return ans 
