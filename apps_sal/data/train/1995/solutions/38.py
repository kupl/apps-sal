class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ends = [i[2] for i in trips]
        max_ends = max(ends)
        all_stops = [0 for i in range(0, max_ends + 1)]
        for trip in trips:
            l, r = trip[1], trip[2]
            all_stops[l:r] = [i + trip[0] for i in all_stops[l:r]]
            if max(all_stops[l:r]) > capacity:
                return False
        return True
