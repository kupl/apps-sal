class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        sorted_trips = sorted(trips, key=lambda x: x[1])
        print(sorted_trips)
        
        cur_capacity = 0
        left = 0
        location = [0 for i in range(1000 + 1)]
        for trip in trips:
            new_capacity = trip[0]
            new_start, new_end = trip[1], trip[2]
            location[new_start:new_end] = [cap + new_capacity for cap in location[new_start:new_end]]
        # print(location)
        for loc in location:
            if loc > capacity:
                return False
        return True
