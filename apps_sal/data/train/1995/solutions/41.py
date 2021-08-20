class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        dests = [x[2] for x in trips]
        myl = [0 for i in range(max(dests) + 1)]
        for x in trips:
            for c in range(x[1], x[2]):
                myl[c] += x[0]
        for i in myl:
            if i > capacity:
                return False
        return True
