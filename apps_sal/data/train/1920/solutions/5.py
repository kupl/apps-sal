class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.time_map = defaultdict(list)
    
    def binarySearch(self, arr, target):
        low, high = 0, len(arr)-1
        while low <= high:
            mid = low + (high - low)//2
            if arr[mid][0] == target:
                return mid
            elif arr[mid][0] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low-1
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.time_map.get(key, None)
        if not arr: return \"\"
        i = self.binarySearch(arr, timestamp)#bisect.bisect(arr, (timestamp, chr(127)))
        return arr[i][1] if i >= 0 else \"\"


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
