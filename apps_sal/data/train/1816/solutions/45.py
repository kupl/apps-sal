from collections import defaultdict


class Solution:

    def alertNames(self, name: List[str], time: List[str]) -> List[str]:
        li = [[int(t[0:2]) * 100 + int(t[3:]), n] for (t, n) in zip(time, name)]
        li = sorted(li)
        d = defaultdict(int)
        dc = defaultdict(int)
        n = len(name)
        (i, j) = (0, 0)
        ans = 0
        s = set()
        while i <= j and j < n:
            if li[j][0] - li[i][0] == 0:
                d[li[j][1]] = 1
                j += 1
            elif li[j][0] - li[i][0] <= 100:
                d[li[j][1]] += 1
                if d[li[j][1]] >= 3:
                    s.add(li[j][1])
                j += 1
            else:
                d[li[i][1]] -= 1
                i += 1
        return sorted(list(s))
