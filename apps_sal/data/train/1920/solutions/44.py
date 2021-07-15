class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return \"\"
        temp = self.dict[key]
        # print(temp)
        for i in reversed(range(len(temp))):
            if temp[i][1] <= timestamp:
                return temp[i][0]
        
        return \"\"


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
