from collections import defaultdict

class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.store = defaultdict(list) # key : [(time1, value1), (time2, value2), ...]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # binary search
        left = 0
        right = len(self.store[key]) - 1
        
        while left <= right:
            middle = (left + right) // 2
            # we want to find self.store[middle] <= timestamp and (middle == len(self.store[key]) - 1 or self.store[middle + 1] > timestamp)
            if self.store[key][middle][0] <= timestamp:
                if (middle == len(self.store[key]) - 1 or self.store[key][middle + 1][0] > timestamp):
                    return self.store[key][middle][1]
                else:
                    left = middle + 1
            else:
                right = middle - 1
        
        return \"\"


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
