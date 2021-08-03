class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.kv=dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.kv:
            self.kv[key].append((timestamp,value))
        else:
            self.kv[key]=[(timestamp,value)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.kv:
            l=self.kv[key]
            for i in range(len(l)-1,-1,-1):
                if l[i][0]<=timestamp:
                    return l[i][1]
        return ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
