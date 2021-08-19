class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key=lambda x: x[1])
        curr = []
        for i in trips:
            curr.append([i[0], i[2]])
            s = 0
            for c in curr:
                if c[1] <= i[1]:
                    continue
                s += c[0]
            if s > capacity:
                return False
        return True
