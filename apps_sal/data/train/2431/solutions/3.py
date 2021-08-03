class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {}
        count = 0
        if(k < 0):
            return 0
        if(len(nums) == 1 or len(nums) == 0):
            return 0
        dic[nums[0]] = 1
        if(k == 0):
            for i in range(1, len(nums)):
                if(nums[i] in dic and dic[nums[i]] == 1):
                    dic[nums[i]] += 1
                    count += 1
                elif(nums[i] not in dic):
                    dic[nums[i]] = 1
                else:
                    dic[nums[i]] += 1

        else:
            for i in range(1, len(nums)):
                if((nums[i] - k) in dic and nums[i] not in dic):
                    count += 1
                if((nums[i] + k) in dic and nums[i] not in dic):
                    count += 1
                dic[nums[i]] = 1

        return count
