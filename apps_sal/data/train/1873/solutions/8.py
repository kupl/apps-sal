class Solution:
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        start_helper = []
        for i in range(len(start)):
            if start[i] == 'L' or start[i] == 'R':
                start_helper.append((start[i], i))
        end_helper = []
        for i in range(len(end)):
            if end[i] == 'L' or end[i] == 'R':
                end_helper.append((end[i], i))

        if len(start_helper) != len(end_helper):
            return False
        for i in range(len(start_helper)):
            if start_helper[i][0] != end_helper[i][0]:
                return False
            elif start_helper[i][0] == 'L' and start_helper[i][1] < end_helper[i][1]:
                return False
            elif start_helper[i][0] == 'R' and start_helper[i][1] > end_helper[i][1]:
                return False
        return True
