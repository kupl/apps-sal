from bisect import *
class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.d= {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = [(timestamp, value)]
        else:
            self.d[key].append((timestamp,value))
    
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d: return \"\"
        #print (key, tm)
        l, r = 0, len(self.d[key])-1
        
        while l+1<r:
            m = l + (r-l)//2
            if self.d[key][m][0] == timestamp: return self.d[key][m][1]
            if self.d[key][m][0] < timestamp: 
                l = m 
            else: r = m - 1 
        if self.d[key][r][0] <= timestamp: return self.d[key][r][1]
        if self.d[key][l][0] <= timestamp: return self.d[key][l][1]
        # no value with smaller timestamp
        return \"\"


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
