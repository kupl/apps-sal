from collections import OrderedDict


class Solution:

    def sortString(self, s: str) -> str:
        s1 = OrderedDict()
        for i in s:
            if i in s1:
                s1[i] += 1
            else:
                s1[i] = 1
        reverse = 0
        t = []
        s1 = OrderedDict(sorted(s1.items()))
        print(s1)
        while True:
            p = []
            for (key, value) in list(s1.items()):
                if value > 0:
                    s1[key] = value - 1
                    p.append(key)
            if p == []:
                break
            if reverse == 1:
                t += p[::-1]
            else:
                t += p
            reverse = 1 - reverse
            print(t)
        return ''.join(t)
