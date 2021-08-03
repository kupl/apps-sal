class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.hashmap = collections.defaultdict(list) # {Key: [(time, value)]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap: return \"\"
        
        n = len(self.hashmap[key])
        for i in range(n-1,-1,-1):
            t, v = self.hashmap[key][i]
            if t <= timestamp:
                return v
        return \"\"
            
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
