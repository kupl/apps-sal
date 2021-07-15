class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        occupied = [0 for i in range(1001)]
        for num_passengers, start_location, end_location in trips:
            for i in range(start_location, end_location):
                occupied[i] += num_passengers
        return max(occupied) <= capacity

