class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        stack, count = [], 0
        for x in target:
            m = 0
            while stack and stack[-1] >= x:
                m = max(m, stack.pop() - x)
            count += m
            stack.append(x)
        count += stack[-1]
        return count
