class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        pooling = []
        for num, start, end in trips:
            pooling.extend([[start, num], [end, -num]])
        pooling.sort()

        for loc, num in pooling:
            capacity -= num
            if capacity < 0:
                return False
        return True
