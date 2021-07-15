
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        totals = [0] * 1001
        for (passengers, start, end) in trips:
            for x in range(start, end):
                totals[x] += passengers
                if totals[x] > capacity:
                    return False
        return True
