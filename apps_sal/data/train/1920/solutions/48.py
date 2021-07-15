class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.d = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.d[key]
        
        l = 0
        r = len(arr) - 1
        closest = float('inf')
        
        while l <= r:
            mid = l + ((r-l)//2)
            if arr[mid][1] == timestamp:
                return arr[mid][0]
            elif arr[mid][1] < timestamp:
                closest = arr[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return closest if closest != float('inf') else \"\"
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
