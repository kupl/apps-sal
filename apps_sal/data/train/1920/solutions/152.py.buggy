from collections import defaultdict

class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.map = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        pair = (timestamp, value)
        self.map[key].append(pair)

    def get(self, key: str, timestamp: int) -> str:
        def binarysearch(arr, l, r):
            if l >= r:
                if arr[l][0] > timestamp:
                    return arr[max(l-1, 0)]
                return arr[l]
            mid = (l + r) // 2
            if arr[mid][0] < timestamp:
                return binarysearch(arr, mid+1, r)
            else:
                return binarysearch(arr, l, mid-1)

        if key in self.map:
            arr = self.map[key]
            if len(arr) == 0:
                return \"\"
            pair = binarysearch(arr, 0, len(arr)-1)
            if arr[0][0] > timestamp: 
                return \"\"
            else:
                return pair[1]
        return \"\"


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
