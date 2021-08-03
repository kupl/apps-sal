class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.times = defaultdict(list)
        self.values = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.values[key].append(value)
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.times:
            return \"\"
        low = 0
        high = len(self.times[key])
        while low < high:
            mid = high + (low - high) // 2
            if timestamp < self.times[key][mid]:
                high = mid
            elif timestamp > self.times[key][mid]:
                low = mid + 1
            else:
                return self.values[key][mid]
        if high == 0:
            return \"\"
        return self.values[key][low - 1]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
