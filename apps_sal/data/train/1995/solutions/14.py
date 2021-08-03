# dict - get keys - dict.keys()
# dict initialization : dict [key] = val OR dict = [key:value]

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        # sort trips by starting point to process them in correct order to detect overlap
        trips = sorted(trips, key=lambda x: x[1])
        currentPassengerCt = trips[0][0]
        tripList = dict()
        tripList[trips[0][2]] = trips[0][0]

        for idx in range(1, len(trips)):
            numPassengers = trips[idx][0]
            startPt = trips[idx][1]
            endPt = trips[idx][2]

            for prevEndPoint in sorted(tripList.keys()):
                if startPt >= prevEndPoint:
                    # overlaps with 1 or more trips
                    # remove finished trips from tripList
                    # deduct passengers from currentPassengerCt

                    # dont overlap with ANY previous trips, capacity <= target
                    # reset currentPassengerCt
                    # empty tripList
                    currentPassengerCt -= tripList[prevEndPoint]
                    del tripList[prevEndPoint]

            # add current trip to tripList
            # update currentPassengerCt
            if endPt in tripList:
                tripList[endPt] += numPassengers
            else:
                tripList[endPt] = numPassengers
            currentPassengerCt += numPassengers

            # if overlap, then sum(passengers) for all concurrent trips <= capacity
            # if no overlap, #passengers for trip  <= capacity
            # currentPassengerCt exceeded
            if currentPassengerCt > capacity:
                return False

        return True
