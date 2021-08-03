class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(value, timestamp)]
        else:
            self.store[key].append((value, timestamp))
    
    def binarySearch(self, k, t):
        arr = self.store[k]
        i = 0
        j = len(arr)-1
        
        while i <= j:
            mid = (i+j)//2
            
            if arr[mid][1] == t:
                return mid
            
            if arr[mid][1] < t and (mid+1 >= len(arr) or arr[mid+1][1] > t):
                return mid
            
            if arr[mid][1] > t:
                j = mid-1
            else:
                i = mid+1
        return -1
        
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ''
        
        idx = self.binarySearch(key, timestamp)
        if idx == -1:
            return ''
        
        return self.store[key][idx][0]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
