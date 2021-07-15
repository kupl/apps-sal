class TimeMap:

    def __init__(self):
        self.M = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.M[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        A = self.M[key]
        if not A:
            return ''
        left = 0
        right = len(A) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if timestamp == A[mid][0]:
                return A[mid][1]
            if timestamp < A[mid][0]:
                right = mid - 1
            else:
                left = mid + 1
        if right == -1:
            return ''
        return A[right][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

