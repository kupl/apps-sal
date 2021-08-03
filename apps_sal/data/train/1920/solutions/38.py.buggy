class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.dict = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.dict[key]
        n = len(arr)
        
        start = 0
        end = len(arr)
        
        while start < end:
            mid = (start + end) // 2
            if arr[mid][0] <= timestamp:
                start = mid + 1
            elif arr[mid][0] > timestamp:
                end = mid
                
        return \"\" if end == 0 else arr[end-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
