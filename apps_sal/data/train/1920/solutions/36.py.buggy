class TimeMap:
    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.dic = collections.defaultdict(list)
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((timestamp, value))
                

    def get(self, key: str, timestamp: int) -> str:
        arr = self.dic[key]
        n = len(arr)
        
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid][0] <= timestamp:
                left = mid + 1
            elif arr[mid][0] > timestamp:
                right = mid - 1
        
        return \"\" if right == -1 else arr[right][1]
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
