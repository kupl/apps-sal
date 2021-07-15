class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        capacity_needed, hp = 0, []
        for trip in trips:
            while hp and hp[0][0]<=trip[1]:
                end,start,c =heapq.heappop(hp)
                capacity_needed-=c
            capacity_needed+=trip[0]
            if capacity_needed>capacity:
                return False
            heapq.heappush(hp,(trip[2],trip[1],trip[0]))
        return True

