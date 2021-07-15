class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d:
            self.d[key].append([timestamp, value])
        else:
            self.d[key] = [[timestamp, value]]
        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.d[key]
        n = len(arr)
        
        l = 0
        r = n
        
        while l < r:
            mid = (l + r) // 2
            if arr[mid][0] > timestamp:
                r = mid
            elif arr[mid][0] <= timestamp:
                l = mid + 1
        return \"\" if r == 0 else arr[r - 1][1]
            
           
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
