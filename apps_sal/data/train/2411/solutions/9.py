class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = [float('-inf'), float('-inf'), float('-inf')]

        for num in nums:
            if num > stack[0]:
                stack = [num, stack[0], stack[1]]
            elif num < stack[0]:
                if num > stack[1]:
                    stack = [stack[0], num, stack[1]]
                elif num < stack[1]:
                    if num > stack[2]:
                        stack = [stack[0], stack[1], num]

        if stack[-1] == float('-inf'):
            return stack[0]
        return stack[-1]
