class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        d = dict()
        ppl = 0
        for i in trips:
            d[i[1]] = d.get(i[1], 0) + i[0]
            for j in range(i[1] + 1, i[2]):
                d[j] = d.get(j, 0) + i[0]
        for i in list(d.values()):
            if i > capacity:
                return False
        return True
