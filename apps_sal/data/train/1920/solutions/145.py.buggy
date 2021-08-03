class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data or timestamp < self.data[key][0][1]:
            return ''
        low = 0
        high = len(self.data[key])
        while low < high:
            mid = (low + high) // 2
            if self.data[key][mid][1] < timestamp + 1:
                low = mid + 1
            else:
                high = mid
        return self.data[key][low - 1][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
