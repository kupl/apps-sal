\"\"\"
[\"TimeMap\",\"set\",\"set\",\"get\",\"get\",\"get\",\"get\",\"get\"]
[[],[\"love\",\"high\",10],[\"love\",\"low\",20],[\"love\",5],[\"love\",10],[\"love\",15],[\"love\",20],[\"love\",25]]


return [null,null,null,\"\",\"high\",\"high\",\"low\",\"low\"]
\"\"\"
class TimeMap:

    def __init__(self):
        self.t = {}
        self.d = collections.defaultdict(list)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((value, timestamp))
        if (key, value) not in self.t:
            self.t[(key, value)] = (timestamp, timestamp)
        else:
            self.t[(key, value)] = (self.t[(key, value)][0], timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        # print(self.t, self.d)
        values = self.d[key]
        n = len(values)
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if values[m][1] == timestamp:
                return values[m][0]
            if values[m][1] < timestamp:
                l = m + 1
            else:
                r = m
        # print(l)
        if values[l][1] == timestamp:
            return values[l][0]
        if l > 0 and values[l][1] > timestamp and values[l - 1][1] < timestamp:
            return values[l - 1][0]
        if values[l][1] > timestamp < values[0][1]:
            return ''
        return values[-1][0]
                


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
