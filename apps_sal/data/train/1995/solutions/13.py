class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips_pickup = sorted(trips,key=lambda x:x[1])
        trips_drop = sorted(trips,key=lambda x:x[2])
        passengers = 0
        i=0
        j=0
        while(i<len(trips)):
            if trips_pickup[i][1] <trips_drop[j][2]:
                passengers +=trips_pickup[i][0]
            else:
                passengers-=trips_drop[j][0]
                j+=1
                continue
            i+=1
            if passengers>capacity:
                return False
        return True
