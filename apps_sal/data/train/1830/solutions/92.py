from heapq import heappush, heappop


class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        appears = dict()
        for i in range(len(rains)):
            if not rains[i]:
                continue
            if not rains[i] in appears:
                appears[rains[i]] = []
            appears[rains[i]].append(i)
        next_rain = dict()
        for v in appears.values():
            for i in range(len(v) - 1):
                next_rain[v[i]] = v[i + 1]
        h = []
        ans = [-1] * len(rains)
        for i in range(len(rains)):
            if rains[i]:
                if i in next_rain:
                    heappush(h, (next_rain[i], rains[i]))
            elif h:
                (day, idx) = heappop(h)
                if day < i:
                    return []
                else:
                    ans[i] = idx
            else:
                ans[i] = 1
        if h:
            return []
        return ans
