class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passengers = [0] * 1000
        for trip in trips:
            (p, start, end) = trip
            for i in range(start, end):
                passengers[i] += p
                if passengers[i] > capacity:
                    return False
        return True
