class Solution:
    """
    def avoidFlood(self, rains: List[int]) -> List[int]:
        from bisect import bisect_left
        wet = {}
        ans = [1]*len(rains)
        dry = []
        for k in range(len(rains)):
            if not rains[k]:
                dry.append(k)
            else:
                ans[k] = -1
        for k in range(len(rains)):
            if rains[k] > 0:
                if rains[k] not in wet:
                    wet[rains[k]] = k
                else:
                    index = bisect_left(dry, wet[rains[k]])
                    if index == len(dry) or dry[index] > k:
                        return []
                    wet[rains[k]] = k
                    ans[dry[index]] = rains[k]
                    dry.pop(index)
        return ans
    """
    '\n    def avoidFlood(self, rains: List[int]) -> List[int]:\n        from sortedcontainers import SortedList\n        wet = {}\n        ans = [1]*len(rains)\n        dry = SortedList()\n        for k in range(len(rains)):\n            if not rains[k]:\n                dry.add(k)\n            else:\n                ans[k] = -1\n        for k in range(len(rains)):\n            if rains[k] > 0:\n                if rains[k] not in wet:\n                    wet[rains[k]] = k\n                else:\n                    index = dry.bisect_left(wet[rains[k]])\n                    if index == len(dry) or dry[index] > k:\n                        return []\n                    wet[rains[k]] = k\n                    ans[dry[index]] = rains[k]\n                    dry.pop(index)\n        return ans\n    '

    def avoidFlood(self, rains: List[int]) -> List[int]:
        from collections import deque
        import heapq
        city = {}
        ans = [1] * len(rains)
        for k in range(len(rains)):
            if rains[k]:
                if rains[k] not in city:
                    city[rains[k]] = deque()
                city[rains[k]].append(k)
                ans[k] = -1
        option = []
        wet = {}
        for k in range(len(rains)):
            if rains[k]:
                if rains[k] in wet:
                    return []
                else:
                    wet[rains[k]] = k
                    city[rains[k]].popleft()
                    if city[rains[k]]:
                        heapq.heappush(option, (city[rains[k]][0], rains[k]))
            elif option:
                (_, c) = heapq.heappop(option)
                ans[k] = c
                wet.pop(c)
            else:
                ans[k] = 1
        return ans
