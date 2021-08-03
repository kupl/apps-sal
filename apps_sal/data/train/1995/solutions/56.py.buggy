class Solution:
    \"\"\"
    return false when a pickup exceeds capacity
    pickup & drop off can happen at same location
    [2,1,5]
    car = 4, 4, 
    
    
    create pickup_dict = {start_location : [[num_passenger = trip[0], end_location=trip[2]]]}
    dropoff_dict = {drop_off location : num_passengers}
    car = [0]*capacity
    car is full when all elem in car > 0
    
    for location in locations:
        decement remaining for passengers in car (make sure no negatives)
        check if location is a pickup:
            if capacity full:
                return false
            else:
                update car
    return True
    
    \"\"\"
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pickups = {} # start location : [[num_passengers]
        drops = {} # drop location: num
        for trip in trips:
            pickups[trip[1]] = pickups.get(trip[1], 0)+trip[0]
            drops[trip[2]] = drops.get(trip[2],0)+trip[0]
        
        count_passengers = 0
        for start in range(1001):
            if start in pickups.keys():
                count_passengers += pickups[start]
                # increment passenger count
            if start in drops.keys():
                count_passengers -= drops[start]
            if count_passengers > capacity:
                return False
        return True

