class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.store = {}
        self.times = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store: 
            self.store[key] = [value]
            self.times[key] = [timestamp]
        else:
            self.store[key].append(value)
            self.times[key].append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store: return \"\"
        else:
            lst = self.times[key]
            
            if timestamp < lst[0]: return \"\"
            elif timestamp >=lst[-1]: return self.store[key][-1]
            else:
                l = 0
                r = len(lst)-1
                while l < r:
                    mid = (l+r)//2
                    if lst[mid] < timestamp: r = mid
                    elif lst[mid] == timestamp: return self.store[key][mid]
                    else: l = mid
                        
                
            
            return self.store[key][r]
                


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
