import heapq
from collections import deque, defaultdict


class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        ret = [-1 for i in rains]
        rain_days = defaultdict(deque)
        for (i, lake) in enumerate(rains):
            if lake != 0:
                rain_days[lake].append(i)
        to_drain = []
        for (i, lake) in enumerate(rains):
            if lake == 0:
                if len(to_drain) == 0:
                    ret[i] = 1
                else:
                    (day, lake) = heapq.heappop(to_drain)
                    if day < i:
                        return []
                    ret[i] = lake
            elif len(rain_days[lake]) > 1:
                rain_days[lake].popleft()
                heapq.heappush(to_drain, (rain_days[lake][0], lake))
        if len(to_drain) > 0:
            return []
        return ret
