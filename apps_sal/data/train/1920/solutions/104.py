#Binary Search (bisect_right) to find item less than or equal to given key 
from bisect import bisect_right
class TimeMap:

    def __init__(self):
        self.keys = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = []
        
        self.keys[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys: return \"\"
        
        values = self.keys[key]
        
        #Or, use [timestamp, chr(127)] to avoid coding binary search
        index = bisect_right(values, [timestamp, chr(127)])
        
        #nothing smaller than or equal to timestamp
        if index == 0: return \"\"
        
        return values[index - 1][1]
    

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
