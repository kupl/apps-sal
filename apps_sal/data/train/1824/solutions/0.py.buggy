def bs(arr, val, key=lambda x:x):
     l, r = 0, len(arr)-1
     if key(arr[l])>val:
         return l
     if key(arr[r])<=val:
         return r+1
     while l+1<r:
         m = (l+r)>>1
         v = key(arr[m])
         if v<=val:
             l = m
         else:
             r = m
     return r
 
 def bs_left(arr, val, key=lambda x:x):
     l, r = 0, len(arr)-1
     if key(arr[l])>=val:
         return l
     if key(arr[r])<val:
         return r+1
     while l+1<r:
         m = (l+r)>>1
         v = key(arr[m])
         if v<val:
             l = m
         else:
             r = m
     return r
             
 
 class Solution:
     def findNumberOfLIS(self, nums):
         if not nums: return 0
         N = len(nums)
         l, dp = 0, [[] for _ in range(N)]
         for n in nums:
             idx1 = bs_left(dp, n, lambda _:_[-1][0] if _ else sys.maxsize)
             if idx1==l:
                 l += 1
             if idx1==0:
                 dp[0].append([n, (dp[0][-1][1] if dp[0] else 0)+1])
             else:
                 idx2 = bs(dp[idx1-1], -n, lambda _:-_[0])
                 dp[idx1].append([n, (dp[idx1][-1][1] if dp[idx1] else 0)+(dp[idx1-1][-1][1] if idx2==0 else (dp[idx1-1][-1][1]-dp[idx1-1][idx2-1][1]))])
         return dp[l-1][-1][1]
