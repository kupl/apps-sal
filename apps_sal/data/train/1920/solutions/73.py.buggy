class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.key_value = collections.defaultdict(list)
        self.time_of_key = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        self.key_value[key].append(value)
        self.time_of_key[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        
        idx = bisect.bisect(self.time_of_key[key], timestamp)
        if idx == 0:
            return ''
        else:
            return self.key_value[key][idx - 1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
