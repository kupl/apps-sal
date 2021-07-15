class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.m = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        A = self.m.get(key, None)
        if not A:
            return \"\"
        i = bisect.bisect(A, (timestamp, chr(123)))
        return A[i-1][1] if i else \"\"
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
