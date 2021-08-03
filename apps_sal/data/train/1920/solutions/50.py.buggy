class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        
        self.dict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key in self.dict:
            self.dict[key].append((timestamp, value))
        else:
            self.dict[key] = [(timestamp, value)]
        

    def get(self, key: str, timestamp: int) -> str:
        
        if key in self.dict:
            arr = self.dict[key]
            
            # do a binary search to find the largest val with t smaller than the timestamp
            
            l = 0
            r = len(arr) -1
            while l <= r:
                mid = l + (r-l)//2
                if arr[mid][0] <= timestamp and (mid+1 >= len(arr) or arr[mid+1][0] > timestamp):
                    # found the largest one:
                    return arr[mid][1]
                elif arr[mid][0] <= timestamp:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return \"\"


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
