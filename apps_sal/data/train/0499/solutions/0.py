class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        prev = -1
        ans = 0
        for num in target:
            if prev == -1:
                prev = num
                ans += num
                continue
            if num > prev:
                ans += (num - prev)
            prev = num
        return ans
