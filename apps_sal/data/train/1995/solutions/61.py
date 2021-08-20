class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key=lambda x: x[1])
        pos = 0
        curr_capacity = capacity
        ht = {}
        for trip in trips:
            for prev in ht:
                if prev <= trip[1]:
                    curr_capacity += ht[prev]
                    ht[prev] = 0
            if trip[0] > curr_capacity:
                return False
            if trip[2] not in ht:
                ht[trip[2]] = trip[0]
            else:
                ht[trip[2]] += trip[0]
            curr_capacity -= trip[0]
        return True
