class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        self.remainSeats=capacity
        self.tripsOnBoard=[]
        trips = sorted(trips, key=lambda trip:trip[1])
        for trip in trips:
            self.offBoard(trip[1])
            if not self.onBoardTrip(trip):
                return False
        return True
    def offBoard(self, currentLocation: int):
        trips2OffBoard = [trip for trip in self.tripsOnBoard if trip[2]<=currentLocation]
        for trip in trips2OffBoard:
            self.remainSeats += trip[0]
        self.tripsOnBoard = [trip for trip in self.tripsOnBoard if trip[2]>currentLocation]
    
    def onBoardTrip(self, trip: List[int]) -> bool:
        if trip[0]<=self.remainSeats:
            self.remainSeats-=trip[0]
            self.tripsOnBoard.append(trip)
            return True
        else:
            return False

