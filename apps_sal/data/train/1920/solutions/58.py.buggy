class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.keyValue = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.keyValue:
            self.keyValue[key] = [(timestamp, value)]
        else:
            self.keyValue[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # Start binary search
        history = self.keyValue[key]
        l = 0
        r = len(history) - 1
        while l < r:
            mid = (r + l) // 2
            if timestamp < history[mid][0]:
                r = mid - 1
            elif timestamp > history[mid][0]:
                l = mid + 1
            else:
                return history[mid][1]
        if timestamp < history[l][0]:
            return history[l - 1][1] if l - 1 >= 0 else ''
        return history[l][1] if len(history) > 0 else ''
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
