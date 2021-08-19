class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # create a array res, res[i] == passenger at place i
        # go through list and add trips[0] to [trips[1], trips[2])
        # check if max(res) <= capacity, if not, false

        res = [0] * 1000

        for trip in trips:
            passenger, start, end = trip
            for i in range(start, end):
                res[i] += passenger
        return max(res) <= capacity
