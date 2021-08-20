class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
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
                    currentPassengerCt -= tripList[prevEndPoint]
                    del tripList[prevEndPoint]
            if endPt in tripList:
                tripList[endPt] += numPassengers
            else:
                tripList[endPt] = numPassengers
            currentPassengerCt += numPassengers
            print(currentPassengerCt)
            if currentPassengerCt > capacity:
                return False
        return True
