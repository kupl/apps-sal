class Solution:

    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        string_map = map(str, nums)
        for i in string_map:
            if len(i) % 2 == 0:
                count += 1
        return count
