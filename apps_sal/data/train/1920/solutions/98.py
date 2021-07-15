from collections import defaultdict
from bisect import bisect

class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.kv = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv:
            return ''
        i = bisect(self.kv[key], (timestamp,'zz')) - 1
        return self.kv[key][i][1] if i >= 0 else ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
