class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        '''
Logics:
We dry lakes in the order of urgency - Greedy.
Iterating through days, when day i is raining on lake lake, if lake is already full, simply return []; else, push the next raining day for lake to to_empty to queue it for drying.
When day i is sunny, dry the most urgent lake referring to to_empty. Remember to remove it from full.
        '''
        # dic stores the raining day for each lake in ascending order.
        dic = collections.defaultdict(list)
        for day,lake in enumerate(rains):
            dic[lake].append(day)
            
        res = [-1] * len(rains)
        to_empty = [] # index,Min-heap and records the lakes that are full and sorted in urgency order.
        for i in range(len(rains)):
            lake = rains[i]
            if lake:
                if dic[lake] and dic[lake][0] < i:
                    return []
                if dic[lake] and len(dic[lake])>1:
                    heapq.heappush(to_empty,dic[lake][1])
            else:
                if to_empty:
                    res[i] = rains[heapq.heappop(to_empty)]
                    dic[res[i]].pop(0)
                else:
                    res[i] = 1
        return res
