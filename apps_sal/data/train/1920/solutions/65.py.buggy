class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.dd = collections.defaultdict(lambda: [[]])

    def set(self, key: str, value: str, timestamp: int) -> None:
        bisect.insort(self.dd[key][0],timestamp)
        self.dd[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dd:
            return ''
        idx = bisect.bisect(self.dd[key][0], timestamp)
        if idx > len(self.dd[key][0]) or idx == 0:
            return ''
        return self.dd[key][idx]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
