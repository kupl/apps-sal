from collections import defaultdict
from bisect import bisect

class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.kvDict = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kvDict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kvDict:
            return \"\"
        index = bisect(self.kvDict[key], (timestamp, chr(127)))
        if index == 0:
            return \"\"
        else:
            return self.kvDict[key][index-1][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
