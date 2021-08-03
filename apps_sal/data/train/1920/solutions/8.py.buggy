class TimeMap:

    def __init__(self):
        self.timeTable = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeTable[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeTable:
            return \"\"
        i = bisect.bisect(self.timeTable[key],[timestamp+1])-1
        if i == -1:
            return \"\"
        return self.timeTable[key][i][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
