class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        fq = [0]*n
        for l,r in requests:
            fq[l]+=1
            if r<n-1:
                fq[r+1]-=1
        for i in range(n):
            fq[i]=(fq[i-1] if i!=0 else 0)+fq[i]
        nums.sort()
        fq.sort()
        ans = 0
        for v,z in zip(nums,fq):
            ans = (ans+v*z)%(10**9+7)
        return ans

