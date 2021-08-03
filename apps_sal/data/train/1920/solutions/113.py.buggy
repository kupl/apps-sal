#hash, list, binary search
#Runtime: 6308 ms, faster than 5.05%
class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.d[key]
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
        return arr[right-1][1] if 0 <= right-1 < len(arr) else ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
