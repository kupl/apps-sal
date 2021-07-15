class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        end = 0
        inCar = 0
        for i in range(0,len(trips)):
            if trips[i][2] > end:
                end = trips[i][2]
        for i in range(1,end):
            for item in trips:
                if item[2] == i:
                    inCar -= item[0]
                elif item[1] == i:
                    inCar += item[0]
            if inCar > capacity:
                return False
        return True
