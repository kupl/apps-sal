class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
    

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.store.get(key)
        if arr is None:
            return \"\"
        l = 0
        r = len(arr) - 1
        result = \"\"
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid][0] <= timestamp:
                result = arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return result
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
