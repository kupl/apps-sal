class Solution:

    def minNumberOperations(self, target: List[int]) -> int:
        (count, stack) = (0, [0])
        for height in target:
            if stack[-1] > height:
                while stack[-1] > height:
                    stack.pop()
            else:
                count += height - stack[-1]
            stack.append(height)
        return count
