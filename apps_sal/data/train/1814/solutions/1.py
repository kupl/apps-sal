class Solution:

    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        (f, idd, last, res) = ([], -99999, 0, [0] * n)
        for s in logs:
            (a, time, b) = s.split(':')
            (a, b) = (int(a), int(b))
            if time == 'start':
                f.append(a)
                if idd != -99999:
                    res[idd] += b - last
                idd = a
                last = b
            else:
                f.pop()
                res[idd] += b - last + 1
                last = b + 1
                idd = f[-1] if f else -99999
        return res
