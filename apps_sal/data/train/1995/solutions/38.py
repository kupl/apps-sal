class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #cus_num = [i[0] for i in trips]
        #starts = [i[1] for i in trips]
        ends = [i[2] for i in trips]
        max_ends = max(ends)
        all_stops = [0 for i in range(0, max_ends + 1)]
        # print(all_stops)
        for trip in trips:
            l, r = trip[1], trip[2]
            # print(all_stops)
            all_stops[l:r] = [i + trip[0] for i in all_stops[l:r]]
            if max(all_stops[l:r]) > capacity:
                return False
        return True
