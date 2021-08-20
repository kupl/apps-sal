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

    def avoidFlood(self, rains: List[int]) -> List[int]:
        from sortedcontainers import SortedList
        wet = {}
        ans = [1] * len(rains)
        dry = SortedList()
        for k in range(len(rains)):
            if not rains[k]:
                dry.add(k)
            else:
                ans[k] = -1
        for k in range(len(rains)):
            if rains[k] > 0:
                if rains[k] not in wet:
                    wet[rains[k]] = k
                else:
                    index = dry.bisect_left(wet[rains[k]])
                    if index == len(dry) or dry[index] > k:
                        return []
                    wet[rains[k]] = k
                    ans[dry[index]] = rains[k]
                    dry.pop(index)
        return ans
