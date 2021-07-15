def binarySearch(ls, t):
    n = len(ls)
    if len(ls)==0:
        return ''
    lo = 0
    hi = n-1
    while lo<hi:
        mi = (hi+lo)//2
        if ls[mi][1]==t:
            return ls[mi][0]
        elif ls[mi][1]<t:
            if ls[mi+1][1]>t:
                return ls[mi][0]
            lo = mi+1
        else:
            hi = mi-1
    if ls[hi][1]<=t:
        return ls[hi][0]
    else:
        return ''

class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        return binarySearch(self.mp[key], timestamp)


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
