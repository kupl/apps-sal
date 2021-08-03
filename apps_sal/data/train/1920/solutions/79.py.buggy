class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.dic = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dic:
            self.dic[key].append([timestamp, value])
        else:
            self.dic[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        # print(key, timestamp, self.dic)
        if key not in self.dic:
            return ''
        else:
            tmp = self.dic[key]
            l = 0
            r = len(tmp) - 1
            res = -1
            while l <= r:
                m = (l + r) // 2
                if tmp[m][0] == timestamp:
                    res = m
                    break
                elif tmp[m][0] < timestamp:
                    l = m + 1
                else:
                    r = m - 1
            if res < 0:
                if r >= 0:
                    res = r
                else:
                    return ''
                    
            return tmp[res][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
