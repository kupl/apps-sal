class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        d = {}
        for i in trips:
            for j in range(i[1] + 1, i[2] + 1):
                if j not in d:
                    d[j] = i[0]
                else:
                    d[j] += i[0]
        for i in d:
            if d[i] > capacity:
                return 0
        return 1
