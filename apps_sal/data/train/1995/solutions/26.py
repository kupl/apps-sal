class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        length = len(trips)

        count = 0
        queue = []
        for trip in trips:
            num_passengers, start_location, end_location = trip
            while queue and queue[0][2] <= start_location:
                count -= queue[0][0]
                queue = queue[1:]
            queue.append(trip)
            queue.sort(key=lambda x: x[2])
            count += num_passengers
            if count > capacity:
                return False
        return True
