class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if(key in self.dic):
            self.dic[key].append((timestamp, value))
        else:
            self.dic[key] = []
            self.dic[key].append((timestamp, value))

    def get(self, key: str, q: int) -> str:
        if(key not in self.dic):
            return \"\"
        
        search = self.dic[key]
        
        low = 0
        high = len(search) - 1
        
        while(low <= high):
            mid = (low+high) // 2
            
            cond1 = search[mid][0] == q
            cond2 = (mid+1 >= len(search) and search[mid][0] < q)
            cond3 = (mid+1 < len(search) and search[mid][0] < q and search[mid+1][0] > q)
            
            if(cond1 or cond2 or cond3):
                return search[mid][1]
            elif(search[mid][0] > q):
                high = mid - 1
            else:
                low = mid + 1
            
        return \"\"
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
