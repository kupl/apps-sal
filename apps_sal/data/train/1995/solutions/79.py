class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if not trips:
            return True
        firstStop = 1001
        lastStop = -1
        for trip in trips:
            firstStop = min(firstStop, trip[1])
            lastStop = max(lastStop, trip[2])
        stops = [0] * (lastStop - firstStop + 1)
        for trip in trips:
            for i in range(trip[1], trip[2]):
                stops[i - firstStop] += trip[0]
                if stops[i - firstStop] > capacity:
                    return False
        return True
