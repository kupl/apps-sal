import collections


class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.dict = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        lt = self.dict[key]
        low = 0
        high = len(lt) - 1
        while low < high:
            mid = (low + high) // 2
            if timestamp < lt[mid][1]:
                high = mid - 1
            elif timestamp >= lt[mid][1]:
                if timestamp >= lt[mid+1][1]:
                    low = mid + 1
                else:
                    break
        if lt[low][1] <= timestamp:
            return lt[low][0]
        else:
            return \"\"
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
