class Solution:

    def repeatedNTimes(self, qq: List[int]) -> int:
        stack = []
        for i in qq:
            if i not in stack:
                stack.append(i)
            else:
                return i
