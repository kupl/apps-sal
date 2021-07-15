class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        return next((v for v,t in reversed(self.d[key]) if t <= timestamp), \"\")
    
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
