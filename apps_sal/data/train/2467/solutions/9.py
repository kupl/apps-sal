class Solution:

    def specialArray(self, nums: List[int]) -> int:
        for i in range(1, 1001):
            geq = 0
            for n in nums:
                geq += n >= i
            if geq == i:
                return i
        return -1
