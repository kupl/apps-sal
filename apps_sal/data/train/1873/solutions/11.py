class Solution:
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if start.replace("X", "") != end.replace("X", ""):
            return False
        import operator

        for char, op in (('L', operator.gt), ('R', operator.lt)):
            j = 0
            for i, c in enumerate(start):
                if c == char:
                    while j < len(end):
                        if end[j] == char and op(j, i):
                            return False
                        elif end[j] == char:
                            j += 1
                            break
                        j += 1

        return True
