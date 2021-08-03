class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append([timestamp,value])
        
        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.dict[key]
        n = len(arr)-1
        l = 0
        r = n
        while l <= r:
            mid = (l+r)//2
            if arr[mid][0] < timestamp:
                l = mid+1
            elif arr[mid][0] > timestamp:
                r = mid-1
            else:
                return arr[mid][1]
        return \"\" if r == -1 else arr[r][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
