import bisect

from collections import defaultdict

class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.kw = defaultdict(list)
        self.kt = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        a = self.kw[key]
        
        if len(a) == 0:
            a.append(value)
            self.kt[key].append(timestamp)
        else:
            i = bisect.bisect_right(self.kt[key], timestamp)
            self.kt[key].insert(i, timestamp)
            self.kw[key].insert(i, value)

    def get(self, key: str, timestamp: int) -> str:
        i = bisect.bisect_right(self.kt[key], timestamp)
        
        if i <= 0:
            return \"\"
        
        return self.kw[key][i - 1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
