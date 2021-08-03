class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        buckets = [0] * 1001
        for trip in trips:
            passengers, start, end = trip
            for i in range(start, end):
                buckets[i] += passengers

        for elem in buckets:
            if elem > capacity:
                return False

        return True
