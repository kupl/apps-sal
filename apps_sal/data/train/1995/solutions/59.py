class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        cap = [capacity] * 1000
        for trip in trips:
            for i in range(trip[1], trip[2]):
                cap[i] -= trip[0]
                if cap[i] < 0:
                    return False
        return True
