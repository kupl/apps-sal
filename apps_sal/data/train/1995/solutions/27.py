class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        r = True
        active = []
        currContent = 0
        maxCapacity = 0
        time = 0
        trips.sort(key=lambda x: x[1])  # sort tips by start time
        lenTrips = len(trips)

        # for each trip
        for i in range(0, lenTrips):  # figure out the capacity required at the start of each trip
            time = trips[i][1]  # set time to start of ith trip

            # add people for ith trip
            currContent += trips[i][0]
            active.append(i)

            # remove people for completed trips
            for j in range(len(active) - 1, -1, -1):
                if trips[active[j]][2] <= time:
                    currContent -= trips[active[j]][0]
                    active.pop(j)

            # track maximum capacity required
            maxCapacity = max(maxCapacity, currContent)

            if maxCapacity > capacity:
                r = False
                break

        return r
