class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        l = target
        stack = []
        total = 0
        for i in range(len(l)):
            if stack and l[stack[-1]] > l[i]:
                total += l[stack[-1]] - l[i]
                while stack and l[stack[-1]] > l[i]:
                    stack.pop()

            if not stack or l[stack[-1]] < l[i]:
                stack.append(i)

            # print(stack, total)
        if stack:
            total += l[stack[-1]]

        return total
