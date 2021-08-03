class TimeMap:

    
    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.t_ = collections.defaultdict(list)
        self.v_ = collections.defaultdict(list)
        self.max_ = collections.defaultdict(int)
        

    def set(self, key, value, timestamp):
        \"\"\"
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        \"\"\"
        self.t_[key].append(timestamp)
        
        self.v_[key].append(value)
        
        self.max_[key] = max(self.max_[key], timestamp)
        

    def get(self, key, timestamp):
        \"\"\"
        :type key: str
        :type timestamp: int
        :rtype: str
        \"\"\"
        if key not in self.t_:
            return \"\"
        if timestamp >= self.max_[key]:
            return self.v_[key][-1]
        v = bisect.bisect_right(self.t_[key], timestamp)
        #print(\"v :\",v)
        if v:
            #print(\"self.v_[key][v - 1] :\",self.v_[key][v - 1])
            return self.v_[key][v - 1]
        return \"\"
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
