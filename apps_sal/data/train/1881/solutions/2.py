class Solution:
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda inter: (inter[1], -inter[0]))
        res = 0
        left, right = -1, -1  # current second largest, and largest
        for inter in intervals:  # assume each inter[0]<inter[1]
            if inter[0] <= left:  # two overlap, skip this inter, cc for intervals with the same inter[1]
                continue  # current inter[0] is not greater than previou inter[0], so at least (left,right) are overlap elements
            if inter[0] > right:  # greater than current largest, no overlap, need add new [left, right]
                res += 2
                right = inter[1]  # greedy, use the two largest num in this inter
                left = right - 1
            elif inter[0] <= right:  # one overlap with current largest
                res += 1
                left = right
                right = inter[1]
        return res
