from collections import defaultdict 
class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.dct = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        arr = self.dct[key]
        if len(self.dct[key]) == 0:
            self.dct[key].append((timestamp, value))
        else:
            lo, hi = 0, len(self.dct[key]) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if arr[mid][0] < timestamp:
                    lo = mid + 1
                else:
                    hi = mid - 1
            arr.insert(lo, (timestamp, value))
        return
            
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dct:
            return \"\"
        arr = self.dct[key]
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] > timestamp:
                hi = mid - 1
            else:
                lo = mid + 1
        return arr[hi][1] if hi != -1 else \"\"
                
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
