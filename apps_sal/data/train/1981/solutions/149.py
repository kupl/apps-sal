class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n=len(nums)
        ind_counts=[0]*n
        nums2=ind_counts.copy()
        for i,j in requests:
            ind_counts[i]+=1
            if j+1<n:
                ind_counts[j+1]-=1
        for i in range(1,n):ind_counts[i]+=ind_counts[i-1]
        nums,ind_count=sorted(nums,reverse=True),sorted(list(range(n)),key=lambda x: -ind_counts[x])
        #print(ind_count)
        i=0
        while i<n and ind_counts[ind_count[i]]>0:
            nums2[ind_count[i]]=nums.pop(0)
            i+=1
        #print(nums2)
        ans=0
        for i in range(1,n):
            nums2[i]+=nums2[i-1]
        for i,j in requests:
            ans+=nums2[j]-nums2[i-1] if i-1>=0 else nums2[j]
        return ans%1000000007
