import collections
class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.storage = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.storage.get(key)
        if not arr:
            return \"\"
        if arr[0][0] > timestamp:
            return \"\"
       
        lft, rht = 0, len(arr) - 1
        while lft <= rht:
            mid = lft + (rht - lft) // 2
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            if arr[mid][0] < timestamp:
                lft = mid + 1
            else:
                rht = mid - 1
        return arr[rht][1]
        
