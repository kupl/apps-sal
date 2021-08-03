class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        init = 1

        while init > 0:
            temp = init
            for i in nums:
                temp = temp + i
                if temp <= 0:
                    break
            else:
                return init

            init += 1
