class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.kv = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        res = self.kv.get(key, [])
        if len(res) == 0:
            res.append((timestamp, value))
        else:
            index = self.bi_search(timestamp, res, 0, len(res)-1) + 1
            res.insert(index, (timestamp, value))
        self.kv[key] = res
    
    def bi_search(self, t: int, values: List, low: int, hi:int) -> int:
        if low > hi:
            return hi
            
        mid = (hi + low) // 2
        if values[mid][0] == t:
            return mid
        elif t > values[mid][0]:
            return self.bi_search(t, values, mid +1, hi) 
        else:
            return self.bi_search(t, values, low, mid -1)
        

    def get(self, key: str, timestamp: int) -> str:
        res = self.kv.get(key, [])
        if len(res) == 0:
            return \"\"
        else:
            index = self.bi_search(timestamp, res, 0, len(res)-1)
        if index == -1:
            return \"\"
        else:
            return res[index][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
