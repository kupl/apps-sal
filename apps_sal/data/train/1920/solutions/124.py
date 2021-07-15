from collections import defaultdict
from bisect import bisect_left
class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.mapping = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapping[key].append((timestamp, value))
        
        
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapping:
            return \"\"
        
        ts = self.mapping[key]
        start, end = 0, len(ts) - 1 
        
        while start + 1 < end:
            mid = (start + end) // 2
            midVal, _ = ts[mid]
            if midVal <= timestamp:
                start = mid 
            else:
                end = mid 
                
        if ts[end][0] <= timestamp:
            return ts[end][1]
        if ts[start][0] <= timestamp:
            return ts[start][1]
        
        return \"\"
            
        
            
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
