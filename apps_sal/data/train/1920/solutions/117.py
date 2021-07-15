class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.keys = collections.defaultdict(list)
        self.times = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append(value)
        self.times[key].append(timestamp)
        
        
    def get(self, key: str, timestamp: int) -> str:
        times = self.times[key]
        
        l, r = 0, len(times)
        while l < r:
            mid = l + (r - l ) // 2
            if timestamp >= times[mid]:
                l = mid + 1
            else:
                r = mid
        return self.keys[key][l-1] if l != 0 else ''
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
