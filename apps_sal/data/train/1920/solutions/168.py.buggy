# 10:45 - 11:30
from collections import defaultdict
from bisect import bisect_right

class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.values = defaultdict(list)
        self.timestamps = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append(value)
        self.timestamps[key].append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        ts = self.timestamps[key]
        index = bisect_right(ts, timestamp)
        if index == 0:
            return ''
        return self.values[key][index - 1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
