from collections import deque, defaultdict


class Solution:

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:

        def time(s):
            (hr, mn) = map(int, s.split(':'))
            return hr * 60 + mn
        ans = set()
        d = defaultdict(deque)
        l = list(zip(keyName, map(time, keyTime)))
        l.sort(key=lambda x: x[1])
        for (k, t) in l:
            d[k].append(t)
            if len(d[k]) == 3 and t - d[k].popleft() <= 60:
                ans.add(k)
        return sorted(ans)
