class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        r = True
        active = []
        currContent = 0
        maxCapacity = 0
        time = 0
        trips.sort(key=lambda x: x[1])
        lenTrips = len(trips)
        for i in range(0, lenTrips):
            time = trips[i][1]
            currContent += trips[i][0]
            active.append(i)
            for j in range(len(active) - 1, -1, -1):
                if trips[active[j]][2] <= time:
                    currContent -= trips[active[j]][0]
                    active.pop(j)
            maxCapacity = max(maxCapacity, currContent)
            if maxCapacity > capacity:
                r = False
                break
        return r
