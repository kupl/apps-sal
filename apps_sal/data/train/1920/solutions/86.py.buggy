class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.map[key]
        if not pairs or pairs[0][0] > timestamp:
            return \"\"
        start, end = 0, len(pairs) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if pairs[mid][0] <= timestamp:
                start = mid
            else:
                end = mid 
        if pairs[end][0] <= timestamp:
            return pairs[end][1]
        if pairs[start][0] <= timestamp:
            return pairs[start][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
