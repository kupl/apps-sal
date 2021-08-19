from collections import defaultdict, deque
import heapq


class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        res = [-1] * len(rains)
        dic = defaultdict(deque)
        for (idx, rain) in enumerate(rains):
            dic[rain].append(idx)
        pq = []
        full = set()
        for i in range(len(rains)):
            if rains[i]:
                if rains[i] in full:
                    return []
                else:
                    full.add(rains[i])
                    dic[rains[i]].popleft()
                if dic[rains[i]]:
                    heapq.heappush(pq, dic[rains[i]][0])
            elif not pq:
                res[i] = 1
            else:
                lake = rains[heapq.heappop(pq)]
                res[i] = lake
                full.discard(lake)
        return res
