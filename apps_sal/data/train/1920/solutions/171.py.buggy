class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.store:
            self.store[key] = [(timestamp, value)]
        else:
            self.store[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        # print(self.store, timestamp)
        
        if key not in self.store:
            return \"\"
        i = bisect.bisect(self.store[key],( timestamp, chr(127)))
        return self.store[key][i-1][1] if i else \"\"
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
