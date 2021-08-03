class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.values, self.times = {}, {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.values:
            self.values[key], self.times[key] = [value], [timestamp]
        elif timestamp > self.times[key][-1]:
            self.values[key].append(value); self.times[key].append(timestamp)
        else:
            i = bisect.bisect_left(self.times[key], timestamp)
            self.values[key].insert(i, value); self.times[key].insert(i, timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.values or timestamp < self.times[key][0]:
            return \"\"
        return self.values[key][bisect.bisect(self.times[key], timestamp)-1]        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
