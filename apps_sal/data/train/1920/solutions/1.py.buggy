class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.times = collections.defaultdict(list)
        self.values = collections.defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp) # append = O(1)
        self.values[key].append(value) # append = O(1)

    def get(self, key: str, timestamp: int) -> str:
        i = bisect.bisect_right(self.times[key],timestamp) # bisect_right = O(logN)
        return self.values[key][i-1] if i else '' # index of dict and then list = O(1) + O(1) = O(1)
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
