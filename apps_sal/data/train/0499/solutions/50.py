class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        bottleneck = 0
        ans = 0
        
        for num in target:
            if num > bottleneck:
                ans += (num-bottleneck)
                bottleneck = num
            else:
                bottleneck = num
        return ans
