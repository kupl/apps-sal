class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.hmap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.hmap[key]
        n = len(arr)
        low = 0
        high = n
        while(low < high):
            mid = (low + high) // 2
            if arr[mid][0] <= timestamp:
                low = mid + 1
            elif arr[mid][0] > timestamp:
                high = mid
        return \"\" if high == 0 else arr[high-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
