class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = {}
        for i, j in enumerate(nums):
            if j not in r:
                r[j] = 1 + 100000 * i
            else:
                r[j] = r[j] % 10000000000 + 1 + 10000000000 * i
        tem = 1
        dist = 500000
        print(r)
        for i in list(r.values()):
            print(i)
            if i % 100000 == tem:
                if tem == 1:
                    dist = 1
                else:
                    dist_tem = i // 10000000000 - (i // 100000) % 100000 + 1
                    if dist_tem < dist:
                        dist = dist_tem
            elif i % 100000 > tem:
                tem = i % 100000
                dist = i // 10000000000 - (i // 100000) % 100000 + 1
        return dist
