class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ind = 0
        for (a, b, c) in trips:
            ind = max(ind, b, c)
        res = [0] * (ind + 1)
        for (a, b, c) in trips:
            for i in range(b, c):
                res[i] += a
        return not any([x > capacity for x in res])
