from collections import defaultdict


class Solution:

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        res = []
        time = defaultdict(list)
        n = len(keyName)
        lst = sorted(list(zip(keyTime, keyName)))
        for (t, k) in lst:
            if k in res:
                continue
            (h, m) = (int(t[:2]), int(t[-2:]))
            if len(time[k]) >= 2:
                (h_0, m_0) = time[k][-2]
                if (h - h_0) * 60 + (m - m_0) <= 60:
                    res.append(k)
                else:
                    time[k].append((h, m))
            else:
                time[k].append((h, m))
        return sorted(res)
