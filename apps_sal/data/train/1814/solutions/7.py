class Solution:

    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        spent = [0 for i in range(n)]
        i = 0
        while len(logs) > 2:
            s1 = logs[i].split(':')
            s2 = logs[i + 1].split(':')
            if s1[1] == 'start' and s2[1] == 'end' and (s1[0] == s2[0]):
                spent[int(s1[0])] += int(s2[2]) - int(s1[2]) + 1
                if i > 0:
                    spent[int(logs[i - 1].split(':')[0])] -= int(s2[2]) - int(s1[2]) + 1
                if i == 0:
                    logs = logs[2:]
                else:
                    logs = logs[0:i] + logs[i + 2:]
                    i -= 1
            else:
                i += 1
        spent[int(logs[0].split(':')[0])] += int(logs[1].split(':')[2]) - int(logs[0].split(':')[2]) + 1
        return spent
