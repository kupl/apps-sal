import collections
from collections import defaultdict
class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.time_map = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        time_map = self.time_map[key]
        left,right = 0, len(time_map)
        
        while left < right:
            mid = left + (right-left) // 2
            if time_map[mid][0] <= timestamp:
                left = mid + 1
            elif time_map[mid][0] > timestamp:
                right = mid
                
        if right != 0:
            return time_map[right-1][1]
        else:
            return \"\"


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
