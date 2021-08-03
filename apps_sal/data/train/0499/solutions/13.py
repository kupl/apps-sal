class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        stack = [0]
        res = 0
        for num in target:
            if num > stack[-1]:
                res += num - stack[-1]
            elif num < stack[-1]:
                while stack[-1] > num:
                    stack.pop()
            stack.append(num)
        return res
