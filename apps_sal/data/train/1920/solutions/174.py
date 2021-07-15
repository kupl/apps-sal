class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.store = {}
    
    def search_time(self,values, time, start, end):
        n = len(values)
        index = int((start + end) / 2)
        if (end - start) <= 3:
            cur = end
            while cur >= start:
                if values[cur][1] <= time:
                    return values[cur][0]
                cur -= 1
            return \"\"
                
        if values[index][1] == time:
            return values[index][0]
        elif values[index][1] < time:
            start = index
        else:
            end = index
        return self.search_time(values, time, start, end)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((value, timestamp))
        else:
            self.store[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            values = self.store[key]
            return self.search_time(values, timestamp, 0, len(values)-1)
        else:
            return \"\"


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
