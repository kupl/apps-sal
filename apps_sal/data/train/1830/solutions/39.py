class Solution:
    # Version 1: Greedy
    # Use binary search to find the first dry day after the city got wet.
    # TC: O(n^2), SC: O(n)
    '''
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
    '''

    # Version 2: Improved version 1
    # Use SortedList to accelerate remove part
    # TC: O(nlogn), SC: O(n)
    '''
    def avoidFlood(self, rains: List[int]) -> List[int]:
        from sortedcontainers import SortedList
        wet = {}
        ans = [1]*len(rains)
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
    '''

    # Version 3: Greedy
    # Store the next position of wet cities in the heap and pop out by urgency
    # TC: O(nlogn), SC: O(n)
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
            else:
                if option:
                    _, c = heapq.heappop(option)
                    ans[k] = c
                    wet.pop(c)
                else:
                    ans[k] = 1
        return ans
