class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trip_start = min([trip[1] for trip in trips])
        trip_end = max([trip[2] for trip in trips])
        trip_register = [0] * (trip_end + 1)
        for trip in trips:
            for idx in range(trip[1], trip[2]):
                trip_register[idx] += trip[0]
        return capacity >= max(trip_register)
