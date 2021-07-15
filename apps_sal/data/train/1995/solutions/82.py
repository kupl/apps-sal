class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ma = float('-inf')
        trips = sorted(trips, key=lambda v: v[1])
        for i in range(len(trips)):
            tmp = 0
            for j in range(i+1):
                if trips[j][2] > trips[i][1]:
                    tmp += trips[j][0]
            ma = max(tmp, ma)
        return ma <= capacity
