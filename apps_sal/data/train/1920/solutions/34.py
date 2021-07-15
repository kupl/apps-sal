from collections import defaultdict

class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.records = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.records[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        item = self.records[key]
        i = len(item)
        while i > 0:
            i -= 1
            if item[i][0] == timestamp:
                return item[i][1]
            elif item[i][0] < timestamp:
                return item[i][1]
        return ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
