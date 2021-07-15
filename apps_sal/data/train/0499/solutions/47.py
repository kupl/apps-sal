class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        stack = []
        count = 0
        target.append(0)
        for num in target:
            while stack and stack[-1] >= num:
                if len(stack) > 1:
                    count += stack[-1] - max(num, stack[-2])
                    stack.pop()
                else:
                    count += stack.pop() - num
            stack.append(num)
        return count
