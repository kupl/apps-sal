class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.dp = {}
    
    def binS(self, key, tar, i, j):
        if i>=j:
            return j
        mid = i + (j-i)//2
        if self.dp[key][mid][1] == tar:
            return mid
        if self.dp[key][mid][1] > tar:
            return self.binS(key, tar, i, mid-1)
        return self.binS(key, tar, mid+1, j)
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dp:
            self.dp[key].append((value, timestamp))
        else:
            self.dp[key] = [(value, timestamp)]
            
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.dp:
            spot = self.binS(key, timestamp, 0, len(self.dp[key]) - 1)
            if spot == 0 and self.dp[key][spot][1] > timestamp:
                return \"\"
            if spot == len(self.dp[key]) or self.dp[key][spot][1] > timestamp:
                spot -= 1
            if self.dp[key][spot][1] > timestamp: return \"\"
            return self.dp[key][spot][0]
        else:
            return \"\"
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
