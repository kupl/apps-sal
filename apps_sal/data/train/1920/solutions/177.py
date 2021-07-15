class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        
        10/02: my
        use dict; 
        
        need to bisect to get the timestamp.  binary search. 
        
        like find first version f
        
        value is an object of [value, list of timestamp. ]
        
        because timesteamp are strictly increasing, so it is monolitically increasing.
        
        1 3 5 7 9  f(4)=3
        
        # BUG Forget self.d self!!!
        
        # BUG max_idx=max(l, max_idx)  max_idx cannot be None, > is not supported between instance of none type and int.
        \"\"\"
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d:
            self.d[key].append((timestamp, value))
        else:
            self.d[key] = [(timestamp, value)]
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.d:
            return self.helper(timestamp, self.d[key])
        else:
            return ''
            
    def helper(self, target, arr):
        # target is the timestamp input
        l,r = 0, len(arr)-1
        max_idx=-1
        while l<=r:
            m = (l+r)//2
            if target==arr[m][0]:
                # there is only 1 timestamp matche due to strictly increasing.
                return arr[m][1]
            # this timestamp is too large, need to find left
            elif arr[m][0]>target:
                r=m-1
            # BUG: mid is a valid one! not left!
            # mid is a valid one! not left! but not sure whether it is the largest
            else:
                l=m+1
                
                max_idx=max(m, max_idx)
        return '' if max_idx==-1 else arr[max_idx][1]  


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
