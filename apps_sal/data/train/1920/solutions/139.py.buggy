from collections import defaultdict
import bisect
class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.cache = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.cache:
            return -1
        
        tsVals = self.cache[key]
        idx = self.binarySearch(tsVals, timestamp)
        #idx = bisect.bisect_left(tsVals, (timestamp, chr(127)))
        
        return tsVals[idx][1] if idx >= 0 else \"\"
    
    def binarySearch(self, tsVals, timestamp):
        low = 0
        high = len(tsVals)
        
        while low < high:
            mid = low + ((high -low)//2)
            
            if tsVals[mid][0] == timestamp:
                return mid 
            
            if tsVals[mid][0] < timestamp:
                low = mid + 1
            else:
                high = mid
        
        #[foor] [1,bar][4, bar2]        
        return low - 1
    
#         def __init__(self):
#         self.M = collections.defaultdict(list)

#     def set(self, key, value, timestamp):
#         self.M[key].append((timestamp, value))

#     def get(self, key, timestamp):
#         A = self.M.get(key, None)
#         if A is None: return \"\"
#         i = bisect.bisect_left(A, (timestamp, chr(127)))
#         return A[i-1][1] if i else \"\"


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
