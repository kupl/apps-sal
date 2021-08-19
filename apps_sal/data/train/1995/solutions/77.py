class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = [[x[1], x[0]] for x in trips] + [[x[2], -x[0]] for x in trips]
        events.sort()
        n = 0
        for event in events:
            n += event[1]
            if n > capacity:
                return False
        return True
