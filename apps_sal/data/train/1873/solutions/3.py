class Solution:
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        previous = {
            'L': 'X',
            'X': 'R'
        }
        if len(start) != len(end):
            return False
        start = list(start)
        for i in range(len(start)):
            if start[i] == end[i]:
                continue
            elif end[i] == 'R':
                return False
            else:
                cur = end[i]
                if i == len(end) - 1:
                    return False
                for j in range(i + 1, len(end)):
                    if start[j] == cur:
                        p = j
                        while p > i:
                            if start[p - 1] == previous[cur]:
                                p -= 1
                            else:
                                return False
                        start[j] = start[p]
                        start[p] = cur
                        break
        return True
