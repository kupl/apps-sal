import collections
import bisect

class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key, [])
        i = bisect.bisect(values, [timestamp, chr(ord(\"z\")+1)])
        return values[i-1][1] if i > 0 else \"\"


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
