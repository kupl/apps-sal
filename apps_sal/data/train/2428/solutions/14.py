class Solution:

    def singleNumber(self, nums):
        dic = {}
        ans = 0
        for i in range(len(nums)):
            if str(nums[i]) in dic:
                dic[str(nums[i])] += 1
            else:
                dic[str(nums[i])] = 1
        for num in dic:
            if dic[num] == 1:
                ans = int(num)
        return ans
        '\n         :type nums: List[int]\n         :rtype: int\n         '
