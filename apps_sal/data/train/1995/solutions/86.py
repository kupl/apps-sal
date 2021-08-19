class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        d = {}
        for (passengers, start, end) in trips:
            # print(passengers, start, end)
            for i in range(start, end):
                if d.get(i) == None:
                    d[i] = passengers
                    # print(d[i])
                else:
                    d[i] += passengers
                    # print(d[i])

        for x in d:
            if d[x] > capacity:
                return False
        return True
