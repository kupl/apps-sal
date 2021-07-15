class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # data = []
        # for t in trips:
        #     data.append((t[1],1, t[0]))
        #     data.append((t[2], 0, t[0]))
        # data = sorted(data)
        # maxp = 0
        # for d in data:
        #     if d[1] == 0:
        #         maxp -= d[2]
        #     else:
        #         maxp += d[2]
        #     if maxp > capacity: return False
        # return True
    
        passenger = 0
        onboard = defaultdict(int)
        offboard = defaultdict(int)
        for t in trips:
            onboard[t[1]] += t[0]
            offboard[t[2]] += t[0]
        for d in range(10001):
            
            if d in onboard: passenger += onboard[d]
            if d in offboard: passenger -= offboard[d]
            if passenger > capacity: return False
        return True
