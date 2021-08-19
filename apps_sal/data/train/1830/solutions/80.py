class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        last_ids = {}
        next_ids = [0] * len(rains)
        for i in reversed(range(len(rains))):
            if rains[i] > 0:
                if rains[i] in last_ids:
                    next_ids[i] = last_ids[rains[i]]
                last_ids[rains[i]] = i

        prio = []
        result = [-1] * len(rains)
        # print(next_ids)
        for i in range(len(rains)):
            if rains[i] > 0:
                if len(prio) > 0 and prio[0] <= i:
                    #print('exit', prio)
                    return []
                if next_ids[i] > 0:
                    #print(i, 'push', next_ids[i])
                    heapq.heappush(prio, next_ids[i])
            else:
                if len(prio) > 0:
                    result[i] = rains[heapq.heappop(prio)]
                    #print(i, 'pop', result)
                else:
                    result[i] = 1
        return result
