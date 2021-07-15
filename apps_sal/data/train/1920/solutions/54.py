class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = [[value], [timestamp]]
        else:
            self.dict[key][0].append(value)
            self.dict[key][1].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict or timestamp < self.dict[key][1][0]:
            return \"\"
        timestamps = self.dict[key][1]
        left = 0
        right = len(timestamps) - 1
        while left <= right:
            mid = (left + right) // 2
            if timestamp >= timestamps[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return self.dict[key][0][right]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
