from collections import defaultdict
class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ''
        values = self.map[key]
        if values[0][0] > timestamp:
            return ''
    
        l, r = 0, len(values) - 1
        while l < r:
            mid = l + (r - l + 1) // 2
            if values[mid][0] > timestamp:
                r = mid - 1
            else:
                l = mid
        
        return values[r][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
