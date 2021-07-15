from collections import defaultdict

class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        lst = self.store[key]
        #for ls in lst[::-1]:
        #    if ls[0] <= timestamp:
        #        return ls[1]
        left, right = 0, len(lst) -1
        clsInd = -1
        while left <= right:
            mid = (left + right) // 2
            t = lst[mid][0]
            if t <= timestamp:
                clsInd = max(clsInd, mid)
                left = mid + 1
            else:
                right = mid -1
                
        return \"\" if clsInd == -1 else lst[clsInd][1]
    

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
