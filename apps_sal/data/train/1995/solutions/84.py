class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        d = {}
        for (passengers, start, end) in trips:
            for i in range(start, end):
                if d.get(i) == None:
                    d[i] = passengers
                else:
                    d[i] += passengers

        for x in d:
            if d[x] > capacity:
                return False
        return True
