from collections import defaultdict
class TimeMap:
    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.map[key]
        left = 0
        right = len(arr) - 1
        if arr[left][0] > timestamp:
            return \"\"
        elif arr[right][0] <= timestamp:
            return arr[right][1]
        else:
            # Binary search
            while left <= right:
                mid = (left + right) // 2
                if arr[mid][0] == timestamp:
                    return arr[mid][1]
                elif arr[mid][0] < timestamp:
                    left = mid + 1
                else:
                    right = mid - 1
            return arr[right][1]
        return \"\"

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
