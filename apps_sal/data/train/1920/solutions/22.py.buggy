class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        bisect.insort(self.d[key], (timestamp, 0, value)) 

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect.bisect(self.d[key], (timestamp, 1, \"\")) - 1
        # print(self.d[key], idx)
        if idx < 0:
          return \"\"
        return self.d[key][idx][2]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
