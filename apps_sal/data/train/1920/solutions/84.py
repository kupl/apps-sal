class TimeMap:
    def __init__(self):
        self.dic = collections.defaultdict(list)
        

    def set(self, key, value, timestamp):
        self.dic[key].append([timestamp, value])

    def get(self, key, timestamp):
        arr = self.dic[key]
        n = len(arr)
        
        left = 0
        right = n-1
        
        while left <= right:
            
            
            mid = left + (right - left) // 2
            if arr[mid][0]== timestamp:
                return arr[mid][1]
            if arr[mid][0] < timestamp:
                left = mid + 1
            elif arr[mid][0] > timestamp:
                right = mid-1
        
        return \"\" if right == -1 else arr[right][1]

        
    
   
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
