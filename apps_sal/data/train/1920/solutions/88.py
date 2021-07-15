class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.keyValueStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyValueStore:
            self.keyValueStore[key] = [(-timestamp,value)]
        else:
            bisect.insort(self.keyValueStore[key],(-timestamp,value))
            

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyValueStore:
            return \"\"
        else:
            for (nts, val) in self.keyValueStore[key]:
                if -nts<=timestamp:
                    return val
            return \"\"
                    
            
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
