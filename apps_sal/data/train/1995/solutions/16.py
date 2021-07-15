import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        trips = sorted(trips, key = lambda k: k[1])
        
        
        car_passengers = 0
        drop_location = []
        
        for trip in trips:
            
            passengers, start_location, end_location = trip
            
            car_passengers += passengers
            
            while len(drop_location) != 0 and heapq.nsmallest(1, drop_location)[0][0] <= start_location:
                print(\"hi\")
                passed_location, drop_passengers  = heapq.heappop(drop_location)
                car_passengers -= drop_passengers
                
            heapq.heappush(drop_location, [end_location, passengers])
            
            if car_passengers > capacity:
                return False
            
            car_passengers = max(car_passengers, 0) # don't want 0
            
        return True
        
