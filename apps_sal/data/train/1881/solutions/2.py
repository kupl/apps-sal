class Solution:

    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda inter: (inter[1], -inter[0]))
        res = 0
        (left, right) = (-1, -1)
        for inter in intervals:
            if inter[0] <= left:
                continue
            if inter[0] > right:
                res += 2
                right = inter[1]
                left = right - 1
            elif inter[0] <= right:
                res += 1
                left = right
                right = inter[1]
        return res
