class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        dic = {}
        stack = []

        for log in logs:
            l = log.split(':')
            if l[1] == 'start':
                if stack:
                    stack[-1][1] += int(l[2]) - stack[-1][2]
                    stack[-1][2] = -1
                    stack += [int(l[0]), 0, int(l[2])],

                else:
                    stack += [int(l[0]), 0, int(l[2])],

            else:
                proc, cumuTime, start = stack.pop()
                dic[proc] = dic.get(proc, 0) + (int(l[2]) - start + 1) + cumuTime
                if stack:
                    stack[-1][2] = int(l[2]) + 1

        return [dic[k] for k in sorted(dic)]
