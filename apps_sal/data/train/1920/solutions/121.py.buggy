class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.map = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        res = self.map[key]
        if not res:
            return \"\"
       
        return self.findFirstSmaller(res, timestamp)
       
    
    def findFirstSmaller(self, nums, target):
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left+right)//2
            if nums[mid][0] < target:
                left = mid
            elif nums[mid][0] == target:
                right = mid
            else:
                right = mid
        if nums[right][0] <= target:
            return nums[right][1]
        if nums[left][0] <= target:
            return nums[left][1]
        return \"\"
        
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
