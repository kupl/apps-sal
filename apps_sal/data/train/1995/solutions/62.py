class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        list_curr = [0] * 1000
        for trip in trips:
            for _ in range(trip[1], trip[2]):
                list_curr[_] += trip[0]
            if max(list_curr) > capacity:
                return False
        return True
