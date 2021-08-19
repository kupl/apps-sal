class Solution:

    def minNumberOperations(self, target: List[int]) -> int:
        r = carry = 0
        for h in target:
            if h > carry:
                r += h - carry
            carry = h
        return r
