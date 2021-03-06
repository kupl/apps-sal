class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if not trips or len(trips) == 0 or capacity == 0:
            return False
        trips.sort(key=lambda x: x[1])
        arr = []
        for (num, start, end) in trips:
            arr.append([start, num])
            arr.append([end, -num])
        arr.sort(key=lambda x: x[0])
        total = 0
        for a in arr:
            total += a[1]
            if total > capacity:
                return False
        return True
