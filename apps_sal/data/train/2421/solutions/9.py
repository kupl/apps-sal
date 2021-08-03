class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        table = {}

        for num in nums:
            if num not in table:
                table[num] = 1
            else:
                table[num] += 1

        sorting_tutple = [(value, key) for key, value in list(table.items())]
        sorting_tutple.sort(reverse=True)

        return sorting_tutple[0][1]
