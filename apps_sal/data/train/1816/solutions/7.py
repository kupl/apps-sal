import datetime as dt
from collections import defaultdict


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        access = defaultdict(list)
        res = set()
        NameTime = []
        for i in range(len(keyName)):
            name = keyName[i]
            h, m = map(int, keyTime[i].split(':'))
            d = dt.datetime(2020, 10, 6, h, m)
            NameTime.append([d, name])
        NameTime.sort()

        period = dt.timedelta(hours=1)
        for d, name in NameTime:
            if name not in res:
                while access[name] and access[name][0] + period < d:
                    access[name].pop(0)
                access[name].append(d)
                if len(access[name]) >= 3:
                    res.add(name)

        return sorted(list(res))
