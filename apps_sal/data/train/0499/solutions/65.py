class Solution:

    def minNumberOperations(self, target: List[int]) -> int:
        r = target[0]
        carry = target[0]
        for i in range(1, len(target)):
            if target[i] > carry:
                r += target[i] - carry
                carry = target[i]
            else:
                carry = target[i]
        return r
