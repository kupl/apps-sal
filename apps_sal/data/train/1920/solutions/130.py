# to store key-value pairs, use a dic. But a key has different values bases on the timestamp. We need something to store the values as well as the timestamp. We can use a queue(or deque)
# because set is in chronological order, time for set is O(1). But for get we need to use binary serach to search the nearest element, so it's O(logn). space is O(n) 
class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.dic = collections.defaultdict(list)
    def search(self,pairs,time):
        l,r = 0,len(pairs)
        while l<r:
            mid = (l+r)//2
            if pairs[mid][0]>time:
                r = mid
            else:
                l = mid+1
        return l
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic or self.dic[key][0][0]>timestamp:
            return ''
        List = self.dic[key]
        index = self.search(List,timestamp)
        return List[index-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
