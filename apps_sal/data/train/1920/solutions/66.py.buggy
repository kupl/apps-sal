class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.dict[key]
        low = -1
        high = len(arr) - 1
        while low < high:
            mid = (low + high + 1) // 2
            if arr[mid][0] > timestamp:
                high = mid - 1
            else:
                low = mid
        return arr[low][1] if low > -1 else ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
