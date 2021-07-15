from bisect import bisect_left as bl, bisect_right as br
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        arr=[]
        for i in range(len(requests)):
            arr.append((requests[i][0],-1))
            arr.append((requests[i][1],1))
        arr.sort()
        freq=[0]*len(nums)
        j=0
        s=0
        for i in range(len(nums)):
            while(j<len(arr) and arr[j][0]==i and arr[j][1]==-1):
                s+=1
                j+=1
            freq[i]=s
            while(j<len(arr) and arr[j][0]==i and arr[j][1]==1):
                s-=1
                j+=1
        freq.sort(reverse=True)
        nums.sort(reverse=True)
        ans=0
        for i in range(len(nums)):
            ans+=(freq[i]*nums[i])%(10**9+7)
        
        return ans%(10**9+7)
        

