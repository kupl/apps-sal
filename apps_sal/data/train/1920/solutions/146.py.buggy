class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        #print(timestamp)
        if key in self.map:
            low = 0
            high = len(self.map[key])-1
            while low <= high:
                middle = (low + high)//2
                if self.map[key][middle][0] == timestamp:
                    return self.map[key][middle][1]
                elif self.map[key][middle][0] < timestamp:
                    low = middle + 1
                else:
                    high = middle - 1
                
            if self.map[key][middle][0] > timestamp:
                if middle > 0: 
                    return self.map[key][middle-1][1]
            else:
                    return self.map[key][middle][1]
                
        return \"\"


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
