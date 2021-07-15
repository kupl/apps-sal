class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.dic = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([timestamp, value])
        
        

    def get(self, key: str, timestamp: int) -> str:
        elements = self.dic.get(key, None)
        if not elements:
            return \"\"
        i = bisect.bisect(elements, [timestamp, chr(200)])
        return elements[i-1][1] if i else \"\"


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
