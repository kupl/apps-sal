class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        stack = []
        for num in arr:
            if len(stack) == 0 or stack[-1] <= num:
                stack.append(num)
            else:
                maxnum = stack.pop()
                while len(stack) > 0 and stack[-1] > num:
                    stack.pop()
                stack.append(maxnum)
        return len(stack)
