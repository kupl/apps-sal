class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        stack = []
        ans = 0
        for n in target:
            if len(stack) != 0 and n <= stack[-1]:
                ans += (stack[-1] - n)
                while len(stack) != 0 and n <= stack[-1]:
                    x = stack.pop()
            stack.append(n)

        if len(stack) != 0:
            ans += stack[-1]
        return ans
