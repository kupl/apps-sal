class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.mapping = collections.defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        lists = self.mapping[key]
        if not lists:
            self.mapping[key] = [(timestamp, value)]
            return
        start, end = 0, len(lists) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if lists[mid][0] == timestamp:
                self.mapping[key][mid] = (timestamp, value)
                return
            elif lists[mid][0] < timestamp:
                start = mid
            else:
                end = mid
                
        # if lists[end][0] == timestamp:
        #     lists[end] = (timestamp, value)            
        #     self.mapping[key] = lists
        #     return
        if lists[end][0] < timestamp:
            lists.insert(end + 1, (timestamp, value))
            self.mapping[key] = lists
            return
        # if lists[start][0] == timestamp:
        #     lists[start] = (timestamp, value)            
        #     self.mapping[key] = lists
        #     return
        if lists[start][0] < timestamp:
            lists.insert(start + 1, (timestamp, value))
            self.mapping[key] = lists
            return
        
        
   

    def get(self, key: str, timestamp: int) -> str:
        lists = self.mapping[key]
        if not lists:
            return ''
        start, end = 0, len(lists) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if lists[mid][0] == timestamp:
                return lists[mid][1]
            elif lists[mid][0] < timestamp:
                start = mid
            else:
                end = mid
                
        if lists[end][0] <= timestamp:
            return lists[end][1]
        if lists[start][0] <= timestamp:
            return lists[start][1]
        return ''
    




# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
