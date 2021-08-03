class Solution:
    def isNStraightHand(self, nums: List[int], W: int) -> bool:
        n = len(nums)

        if n % W != 0:
            return False

        nums.sort()

        dic = OrderedDict()

        for num in nums:
            dic[num] = dic.get(num, 0) + 1

        while len(list(dic.keys())) > 0:
            m = min(dic)
            for i in range(m, m + W):
                val = dic.get(i)

                if not val:
                    return False
                if val == 1:
                    del dic[i]
                else:
                    dic[i] -= 1
        return True
