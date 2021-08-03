class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.dt = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dt:
            self.dt[key] = [(timestamp, value)]
        else:
            self.dt[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dt or self.dt[key][0][0] > timestamp:
            return \"\"
        
        values = self.dt[key]
        left, right = 0, len(values)
        while left < right:
            mid = (left + right) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] > timestamp:
                right = mid
            else:
                left = mid + 1
        
        return values[right-1][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
