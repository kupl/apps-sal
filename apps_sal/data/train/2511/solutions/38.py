from collections import Counter


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        stack = []

        for n in A:
            if n not in stack:
                stack.append(n)
            else:
                return n
