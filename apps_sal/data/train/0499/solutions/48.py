class Solution:

    def minNumberOperations(self, target: List[int]) -> int:
        ans = 0
        stack = [0]
        for num in target:
            max_ = 0
            while stack and stack[-1] >= num:
                max_ = max(max_, abs(stack.pop() - num))
            ans += max_
            stack.append(num)
        while stack[-1]:
            ans += abs(stack.pop() - stack[-1])
        return ans
