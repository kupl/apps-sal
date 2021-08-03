class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        from collections import defaultdict
        self.kv = defaultdict(list)
        z=0

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv[key].append((timestamp, value))
        z=0

    def get(self, key: str, timestamp: int) -> str:
        from bisect import bisect_right
        if key not in self.kv:
            return \"\"
        
        ind = bisect_right(self.kv[key], (timestamp+0.1,\"\"))-1  #  +0.1 to resolve the case when timestamp == timestamp_prev
        if ind == -1:
            return \"\"
        else:
            return self.kv[key][ind][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
