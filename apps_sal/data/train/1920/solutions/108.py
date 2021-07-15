from collections import defaultdict

class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.dict[key]
        
        left = 0
        right = len(arr)
        
        while left < right:
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
                
        return arr[right - 1][1] if right > 0 else ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
