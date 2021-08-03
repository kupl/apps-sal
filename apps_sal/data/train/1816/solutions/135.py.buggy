from typing import List


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        from collections import defaultdict
        d = defaultdict(list)
        names_by_time = sorted(zip(keyName, keyTime), key=lambda t: t[1])
        for name, time in names_by_time:
            d[name].append(time)
        alerts = []
        for name, times in d.items():
            for t1, t2, t3 in zip(times, times[1:], times[2:]):
                t1h, t1m = map(int, t1.split(\":\"))
                t3h, t3m = map(int, t3.split(\":\"))
                if (t1h == t3h) or (t1h + 1 == t3h and t1m >= t3m):
                    alerts.append(name)
                    break
        return sorted(alerts)

