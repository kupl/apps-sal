class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_cnt = 0
        for num in nums:
            if (len(str(num)) % 2 == 0):
                even_cnt += 1

        return even_cnt
