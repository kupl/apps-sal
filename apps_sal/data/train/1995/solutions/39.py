class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        final = 0
        for trip in trips:
            final = max(final, trip[2])
        people = [0] * (final + 1)
        for trip in trips:
            for board in range(trip[1], trip[2]):
                people[board] += trip[0]
        if max(people) > capacity:
            return False
        else:
            return True
