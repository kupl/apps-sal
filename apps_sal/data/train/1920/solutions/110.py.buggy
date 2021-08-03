import bisect
from collections import defaultdict
class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.tkv = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.tkv:
            self.tkv[key][0].append(timestamp)
            self.tkv[key][1].append(value)
        else:
            self.tkv[key] = [[timestamp],[value]]

    def get(self, key: str, timestamp: int) -> str:
        get_index = bisect.bisect_left(self.tkv[key][0], timestamp)
        n = len(self.tkv[key][0])
            
        if get_index > n - 1:
                return self.tkv[key][1][n - 1]
        else: 
            if self.tkv[key][0][get_index] == timestamp:
                return self.tkv[key][1][get_index]
            elif get_index > 0:
                return self.tkv[key][1][get_index - 1]
            else:
                return \"\"


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
