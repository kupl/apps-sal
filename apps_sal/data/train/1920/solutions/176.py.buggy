class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.data = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.data[key]:
            return \"\"
        start = 0
        end = len(self.data[key]) - 1
        while start < end:
            mid = start + (end-start) // 2
            if self.data[key][mid][0] <= timestamp and self.data[key][mid+1][0] > timestamp:
                return self.data[key][mid][1]
            if self.data[key][mid][0] <= timestamp:
                start = mid + 1
            else:
                end = mid - 1
        
        return self.data[key][-1][1] if self.data[key][-1][0] <= timestamp else \"\"


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
