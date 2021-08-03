from sortedcontainers import SortedSet, SortedList
from heapq import heappush, heappop
from datetime import timedelta
from collections import defaultdict, deque


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        users = []
        for i, kt in enumerate(keyTime):
            kts = kt.split(':')
            t = timedelta(hours=int(kts[0]), minutes=int(kts[1]))
            users.append((t, keyName[i]))

        users.sort()
        d = defaultdict(deque)
        barier = timedelta(hours=1)
        rez = SortedSet()
        for k in users:
            if len(d[k[1]]) > 0:
                er = d[k[1]][0]
                while k[0] - er > barier and len(d[k[1]]) > 0:
                    d[k[1]].popleft()
                    if len(d[k[1]]) > 0:
                        er = d[k[1]][0]
            d[k[1]].append(k[0])
            if len(d[k[1]]) >= 3:
                rez.add(k[1])

        return list(rez)
