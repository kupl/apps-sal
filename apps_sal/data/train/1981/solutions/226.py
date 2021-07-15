class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        count = [0]*(n+1)
        for i in range(len(requests)):
            start = requests[i][0]
            end = requests[i][1]
            count[start]+=1
            count[end+1]-=1
        for i in range(1,n):
            count[i]+=count[i-1]
        #print(count)
        x=count.pop()
        nums.sort(reverse=True)
        count.sort(reverse=True)
        #print(nums)
        #print(count)
        ans = 0
        for i in range(n):
            ans+=(count[i]*nums[i])%(10**9+7)
        
        return ans%(10**9+7)

