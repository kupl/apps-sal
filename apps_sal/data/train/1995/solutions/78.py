class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        res = [0] * 1000

        for trip in trips:
            passenger, start, end = trip
            for i in range(start, end):
                res[i] += passenger
        return max(res) <= capacity
