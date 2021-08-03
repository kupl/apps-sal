class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        for i in range(1, 1000000):
            flag = 0
            n = i
            for j in nums:
                n += j
                if n < 1:
                    flag = 1
                    break
            if flag == 0:
                return i
