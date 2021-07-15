class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        total_trip = [0 for _ in range(1000)]
        for tt in trips:
            for loc in range(tt[1],tt[2]):
                total_trip[loc] += tt[0]
        if max(total_trip) <= capacity:
            return True
        return False
