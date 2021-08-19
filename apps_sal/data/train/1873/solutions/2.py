class Solution:

    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        start_pair = [(i, c) for (i, c) in enumerate(start) if c != 'X']
        end_pair = [(i, c) for (i, c) in enumerate(end) if c != 'X']
        if len(start_pair) != len(end_pair):
            return False
        for ((i_start, c_start), (i_end, c_end)) in zip(start_pair, end_pair):
            if c_start != c_end or (c_start == 'L' and i_start < i_end) or (c_start == 'R' and i_start > i_end):
                return False
        return True
