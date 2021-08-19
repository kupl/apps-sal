class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passenger = 0
        onboard = defaultdict(int)
        offboard = defaultdict(int)
        for t in trips:
            onboard[t[1]] += t[0]
            offboard[t[2]] += t[0]
        for d in range(10001):
            if d in onboard:
                passenger += onboard[d]
            if d in offboard:
                passenger -= offboard[d]
            if passenger > capacity:
                return False
        return True
