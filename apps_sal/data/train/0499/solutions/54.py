class Solution:

    def minNumberOperations(self, target: List[int]) -> int:
        target.append(0)
        stack = [0]
        res = 0
        for t in target:
            if t < stack[-1]:
                res += stack.pop() - t
                while stack[-1] > t:
                    stack.pop()
            if t > stack[-1]:
                stack.append(t)
        return res
