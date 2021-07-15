class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        nums.sort()
        counter = [0] * (10 ** 5 + 2)
        
        for start, end in requests:
            counter[start] += 1
            counter[end+1] -= 1
        
        for i in range(1, len(counter)):
            counter[i] += counter[i-1]
        
        counter.sort()
        
        p1 = len(counter) - 1
        p2 = len(nums) - 1
        count = 0
        while counter[p1] > 0:
            count = (count + counter[p1] * nums[p2]) % (10**9+7)
            p1 -= 1
            p2 -= 1
        
        return count
