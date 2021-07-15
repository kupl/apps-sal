class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        #ans = 0
        #for c in Counter(nums).values():
        #    if c > 1:
        #        ans += c * (c-1) // 2
        #return ans
        return sum((c*(c-1)//2 for c in Counter(nums).values()))
