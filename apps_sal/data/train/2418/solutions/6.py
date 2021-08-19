class Solution:

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        diction = {}
        flag = 0
        for number in nums:
            if number not in diction:
                diction[number] = 1
            else:
                flag = 1
                break
        if flag == 1:
            return True
        else:
            return False
