from collections import defaultdict

class TimeMap:
    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if not self.data[key]:
            return \"\"
        left, right = 0, len(self.data[key]) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if timestamp == self.data[key][mid][0]:
                left = mid + 1
            elif timestamp > self.data[key][mid][0]:
                left = mid + 1
            elif timestamp < self.data[key][mid][0]:
                right = mid - 1
        
        if right == -1 or self.data[key][right][0] > timestamp:
            return \"\"
        return self.data[key][right][1]
                
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
