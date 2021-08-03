class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        from collections import defaultdict
        import bisect
        # Key value pairs of (keys, list of (timestamp, value) tuples)
        # Binary search to find the value in O(log n) time
        self._store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not self._store[key]:
            return \"\"
        idx = self.bsearch(self._store[key], timestamp)
        if self._store[key][idx][0] > timestamp and idx - 1 >= 0:
            idx -= 1
        temp = self._store[key][idx]
        return temp[1] if temp[0] <= timestamp else \"\"
    
    def bsearch(self, arr, timestamp):
        lo = 0
        hi = len(arr) - 1
        
        while lo < hi:
            mid = (lo + hi)//2
            if arr[mid][0] < timestamp:
                lo = mid + 1
            else:
                hi = mid
        return lo


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
