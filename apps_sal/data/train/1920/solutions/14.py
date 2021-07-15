class TimeMap:

    def __init__(self):
        self.values = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.values:
            self.values[key] = []
            
        self.values[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.values:
            return \"\"
        
        if timestamp < self.values[key][0][1]:
            return \"\"
        
        return self.search(key, 0, len(self.values[key]) - 1, timestamp)
    
    def search(self, key, left, right, timestamp):
        mid = (left + right) // 2

        if self.values[key][mid][1] == timestamp:
            return self.values[key][mid][0]
        
        if left > right:
            return self.values[key][right][0]
        
        if self.values[key][mid][1] > timestamp:
            return self.search(key, left, mid - 1, timestamp)
        else:
            return self.search(key, mid + 1, right, timestamp)
            
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
