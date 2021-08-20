class Solution:

    def minNumberOperations(self, target: List[int]) -> int:
        ret = 0
        carry = 0
        for i in range(len(target)):
            e = target[i]
            ret += max(0, e - carry)
            carry = e
        return ret
