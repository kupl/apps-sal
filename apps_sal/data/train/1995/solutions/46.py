from collections import defaultdict, OrderedDict


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key=lambda x: x[1])
        passengers = 0

        dropoffs = defaultdict(int)
        for i in range(len(trips)):
            dropoffs[trips[i][2]] += trips[i][0]
        dropoffs = OrderedDict(sorted(dropoffs.items()))

        for lis in trips:
            passengers += lis[0]
            for key in dropoffs:
                if lis[1] >= key:
                    passengers -= dropoffs[key]
                    dropoffs[key] = 0
            if passengers > capacity:
                return False
        return True
