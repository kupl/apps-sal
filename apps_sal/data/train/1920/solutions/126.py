from collections import defaultdict

class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.storage = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage:
            return \"\"
        
        returned = self.storage[key]
        l = 0
        r = len(returned)
        
        while l < r:
            mid = l + (r - l) // 2
            
            if returned[mid][1] <= timestamp:
                l = mid + 1
            elif returned[mid][1] > timestamp:
                r = mid
                
        return \"\" if r == 0 else returned[r - 1][0]
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
