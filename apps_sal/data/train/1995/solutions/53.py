from operator import itemgetter


class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        cp_arr = []
        trips = sorted(trips, key=lambda x: x[1], reverse=False)
        min_val = min([i[1] for i in trips])
        max_val = max([i[2] for i in trips])
        offset = max_val - min_val
        check_arr = [0] * offset
        for trip in trips:
            low = trip[1]
            high = trip[2]
            for i in range(low, high):
                check_arr[i - offset] += trip[0]
        if max(check_arr) <= capacity:
            return True
        return False
