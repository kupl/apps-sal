class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        tup = (timestamp, value)
        if key in self.store:
            # idx = bisect.bisect_left(self.store[key], tup)
            self.store[key].append(tup)
        else:
            self.store[key] = [tup]

    def get(self, key: str, timestamp: int) -> str:
        #do binary search
        low = 0
        high = len(self.store[key])-1
        arr = self.store[key]
        
        while high != low:
            curr = (low + high)//2
            if arr[curr][0] == timestamp:
                return arr[curr][1]
            elif arr[curr][0] < timestamp:
                low = min(len(arr)-1, curr + 1)
            elif arr[curr][0] > timestamp:
                high = max(0,curr - 1)
           
        curr = (low + high)//2
        
        if arr[high][0] <= timestamp:
            return arr[high][1]
        elif high - 1 >= 0:
            if arr[high-1][0] <= timestamp:
                return arr[high-1][1]
        else:
            return \"\"
                
            
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
