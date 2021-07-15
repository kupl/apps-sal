class TimeStampOrder :
    def __init__(self, tim, val):
        self.ord_tim = [tim]
        self.tim_dict = {tim:val}

    def insert(self, tim, val):
        self.tim_dict[tim] = val
        i = 0
        while i < len(self.ord_tim):
            if tim > self.ord_tim[i]:
                break
            i+=1
        self.ord_tim.insert(i,tim)

    def get(self, tim):
        i = 0
        while i < len(self.ord_tim):
            if tim >= self.ord_tim[i]:
                return self.tim_dict[self.ord_tim[i]]
            i+=1
        return \"\"
class TimeMap:
    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.dict_key = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict_key:
            self.dict_key[key] = TimeStampOrder(timestamp,value)
        else :
            self.dict_key[key].insert(timestamp,value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict_key:
            return \"\"
        else :
            return self.dict_key[key].get(timestamp)


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
