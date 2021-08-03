class TimeMap:

    from collections import defaultdict
    
    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        
        self.cache = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        self.cache[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.cache:
            return ''
        
        key_val_list = self.cache[key]
        
        # print(self.cache)
        
        l = 0
        r = len(key_val_list) - 1
        
        # find idx where key_val_list[i][0] <= timestamp
        
        if key_val_list[l][0] > timestamp:
            return ''
        
        found = None
        
        while r >= l:
            m = (r + l) // 2
            
            if key_val_list[m][0] > timestamp:
                r = m - 1
            elif key_val_list[m][0] == timestamp:
                return key_val_list[m][1]
            else:
                found = m
                l = m + 1
        
        return key_val_list[found][1]
        
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
