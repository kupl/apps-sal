class TimeMap:

    def __init__(self):
        self.key = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key:
            self.key[key] = [[value],[timestamp]]
        else:
            self.key[key][0].append(value)
            self.key[key][1].append(timestamp)
        # print(self.key)

    def get(self, key: str, timestamp: int) -> str:
        value,t = self.key[key]
        low=0
        high=len(t)-1
        while low<high:
            mid = (low+high)//2
            if timestamp < t[high]:
                high = mid - 1
            else:
                low = mid + 1
        if t[low] <= timestamp:
            return value[low]
        else:
            return \"\"
            

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
