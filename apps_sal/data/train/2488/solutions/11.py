class Solution:
    def digits(self, num):
        count = 0
        while num:
            num = num // 10
            count += 1
        if count % 2 == 0:
            return True
        else:
            return False

    def findNumbers(self, nums: List[int]) -> int:
        c = 0
        for i in nums:
            if Solution().digits(i):
                c += 1
        return c
