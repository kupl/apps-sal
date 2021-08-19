class Solution:

    def numIdenticalPairs(self, nums: List[int]) -> int:
        for i in nums:
            repeat = {}
            n = 0
            for i in nums:
                if i in repeat:
                    n += repeat[i]
                    repeat[i] += 1
                else:
                    repeat[i] = 1
        return n
