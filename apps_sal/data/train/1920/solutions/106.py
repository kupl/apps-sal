
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


class TimeMap:
    def __init__(self):
        self.d = {}

    def set(self, key, value, timestamp):
        self.d.setdefault(key, []).append([timestamp, value])

    def get(self, key, timestamp):
        v = self.d.get(key, [])
        i = bisect.bisect_right(v, [timestamp, chr(ord('z')+1)])
        return v[i-1][1] if i else ''
