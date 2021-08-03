from collections import defaultdict
class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.mapping = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapping[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        i = bisect.bisect_right(self.mapping[key], (timestamp, chr(127)))
        if i:
            return self.mapping[key][i-1][1]
        return \"\"


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
