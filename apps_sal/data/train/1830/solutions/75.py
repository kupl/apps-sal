from queue import PriorityQueue
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        pq = PriorityQueue()
        rainOnLake = {}        
        for i, v in enumerate(rains):
            if v > 0:
                if v not in rainOnLake: rainOnLake[v] = []
                rainOnLake[v].append(i)
        
        lakes = {}
        ans = [-1] * len(rains)
        for i , v in enumerate(rains):
            if v > 0:
                if lakes.get(v, 0) > 0: 
                    return []
                lakes[v] = 1
                rainSched = rainOnLake[v]
                rainSched.pop(0)
                if rainSched:
                    nextRain = rainSched[0]
                    pq.put((nextRain, v))
            elif v == 0:
                if pq.qsize() <= 0:
                    ans[i] = 111111111
                else:
                    (d, l) = pq.get()
                    ans[i] = l
                    lakes[l] = 0
        return ans
                

