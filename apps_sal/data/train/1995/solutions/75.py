class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        kmlist = {}
        trips.sort(key=lambda x: (x[1], x[2]))
        for trip in trips:
            for i in range(trip[1], trip[2]):
                if i in kmlist:
                    kmlist[i] += trip[0]
                else:
                    kmlist[i] = trip[0]
        maxval = max(kmlist.values())
        return maxval <= capacity
