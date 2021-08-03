class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trip_travel = []
        for passengers, start, end in trips:
            trip_travel.append((start, passengers, 1))  # start times so adding people
            trip_travel.append((end, passengers, 0))  # start times so removing people

        trip_travel.sort(key=lambda x: (x[0], x[2]))  # sort and make sure removing people(increase capacity) before adding people - that way if adding and removing at same location-capacity not temporarily < 0
        for travel in trip_travel:
            if travel[2] == 1:
                capacity -= travel[1]
            else:
                capacity += travel[1]

            if capacity < 0:
                return False

        return True
