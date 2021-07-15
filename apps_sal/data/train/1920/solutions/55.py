import bisect as b
from collections import defaultdict
class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.timestamps = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.timestamps.get(key)
        if not arr: return \"\"
        i = b.bisect(arr, (timestamp, chr(127)))
        return arr[i-1][1] if i else \"\"


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
