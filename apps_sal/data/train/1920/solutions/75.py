class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.hashmap = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))
        return 

    def get(self, key: str, timestamp: int) -> str:
        index = bisect.bisect(self.hashmap[key], (timestamp, chr(ord(\"z\") + 1)))
        if index != 0:
            return self.hashmap[key][index - 1][1]
        return \"\"


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
