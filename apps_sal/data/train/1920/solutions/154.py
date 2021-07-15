from collections import defaultdict

class Node:
    def __init__(self,time,val):
        self.left = None
        self.right = None
        self.time = time
        self.val = val
        

class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.dic = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic.keys(): return \"\"
        
        l, r = 0, len(self.dic[key])-1
        
        while l+1 < r:
            mid = (l + r) // 2
                
            if self.dic[key][mid][0] == timestamp:
                return self.dic[key][mid][1]
            elif self.dic[key][mid][0] < timestamp:
                l = mid
            else:
                r = mid
                
        if self.dic[key][r][0] <= timestamp:
            return self.dic[key][r][1]
        if self.dic[key][l][0] <= timestamp:
            return self.dic[key][l][1]
        
        return \"\"

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
