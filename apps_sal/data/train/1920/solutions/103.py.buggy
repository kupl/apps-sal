class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        # https://leetcode.com/problems/time-based-key-value-store/discuss/595719/python-very-simple-98-fast
        self.val_dict = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.val_dict[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.val_dict:
            return \"\"
        val_list  = self.val_dict[key]
        i = len(val_list) -1 
        while i >=0 and val_list[i][1] > timestamp:
            i -= 1
        return val_list[i][0] if i >=0 else \"\"
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
