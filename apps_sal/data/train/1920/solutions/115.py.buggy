class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.dict = defaultdict(list) 

    def set(self, key: str, value: str, timestamp: int) -> None:
        # find key and check, set new key if it doesn't exist
        self.dict[key].append((value, timestamp))
            
    def get(self, key: str, timestamp: int) -> str:
        arr = self.dict[key]
        n = len(arr)
        
        left = 0
        right = n
        
        # Short answer
        # v = self.d.get(key, [])
        # i = bisect.bisect_right(v, [timestamp, chr(ord('z')+1)])
        # return v[i-1][1] if i else ''
        
        while left < right:
            mid = (left + right) // 2 
            if arr[mid][1] <= timestamp:
                left = mid + 1
            elif arr[mid][1] > timestamp:
                right = mid
        
        return \"\" if right == 0 else arr[right - 1][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
