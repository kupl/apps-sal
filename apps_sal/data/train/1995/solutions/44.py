class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        d=[0 for i in range(1001)]
        for i in trips:
            for j in range(i[1], i[2]):
                d[j]+=i[0]
        # print(d)
        for i in range(1001):
            if d[i]>capacity:
                return False
        return True
