class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        print(trips)
        start = trips[0][1]
        end = trips[0][2]
        capacity = capacity - trips[0][0]
        if capacity < 0:
            return False
        q = [(trips[0][2], trips[0][0])]
        n = len(trips)
        for trip in trips[1:]:
            s = trip[1]
            dup = q[:]
            while q:
                if q[0][0] <= s:
                    capacity += q[0][1]
                    q.pop(0)
                else:
                    break
            capacity -= trip[0]
            q.append((trip[2], trip[0]))
            q.sort(key=lambda x: x[0])
            if capacity < 0:
                return False
        return True
