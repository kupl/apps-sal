class Solution:
    def specialArray(self, nums: List[int]) -> int:
        cache=set()
        for x in range(len(nums),0,-1):
            cnt=0
            for i in range(len(nums)):
                if nums[i] in cache:
                    cnt+=1
                elif nums[i]>=x:
                    cnt+=1
                    cache.add(nums[i])
            if cnt==x:
                return x
        return -1
