from collections import defaultdict

class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append({
            \"value\": value,
            \"timestamp\": timestamp
        })

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return \"\"

        data = self.data[key]
        n = len(data)

        result = \"\"
        start, end = 0, n - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            if data[mid][\"timestamp\"] > timestamp:
                end = mid - 1
            elif data[mid][\"timestamp\"] < timestamp:
                start = mid + 1
                result = data[mid][\"value\"]
            else:
                return data[mid][\"value\"]
            
        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
