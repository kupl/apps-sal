class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new = [0 for i in range(2001)]
        for i in range(len(nums)):
            new[1000 + nums[i]] = new[1000 + nums[i]] + 1
        count = 0
        product = 1
        digit = []
        for i in range(2000, -1, -1):
            while(new[i] > 0):
                digit.append(i - 1000)
                count = count + 1
                new[i] = new[i] - 1
                if count == 3:
                    break
            if count == 3:
                break
        for i in range(2001):
            while(new[i] > 0):
                digit.append(i - 1000)
                count = count + 1
                new[i] = new[i] - 1
                if count == 5:
                    break
            if count == 5:
                break
        if len(digit) == 3:
            return digit[0] * digit[1] * digit[2]
        elif len(digit) == 4:
            return max(digit[0] * digit[1] * digit[2], digit[3] * digit[1] * digit[2])
        else:
            p1 = digit[0] * digit[3] * digit[4]
            p2 = digit[0] * digit[1] * digit[2]
            return max(p1, p2)
