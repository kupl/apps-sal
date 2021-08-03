class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.d = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = [(timestamp, value)]
        else:
            self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ''
        
        # Binary search
        arr = self.d[key]
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1

        return '' if right == -1 else arr[right][1]
                


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
