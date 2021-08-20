class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        lst = []
        for (people, st, end) in trips:
            lst.append((st, people, 1))
            lst.append((end, people, 0))
        lst.sort(key=lambda x: (x[0], x[2]))
        current = 0
        for (time, people, pickup) in lst:
            if pickup:
                current += people
            else:
                current -= people
            if current > capacity:
                return False
        return True
