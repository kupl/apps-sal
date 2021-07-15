class MajorityChecker:

    def __init__(self, arr: List[int]):
        
        
        self.tables = collections.defaultdict(list)
        for i, num in enumerate(arr):
            self.tables[num].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        
        if right - left + 1 < threshold:
            return -1
        for num in self.tables:
            if len(self.tables[num]) < threshold:
                continue
            l = self.leftSearch(self.tables[num], left)
            r = self.rightSearch(self.tables[num], right)
            # print(num, self.tables[num])
            # print(left, right)
            # print(l, r)
            if r-l  >= threshold:
                return num
        return -1
                
        
        
    def leftSearch(self, array, target):
        
        l = 0
        r = len(array)
        while l < r:
            m = (l+r) // 2
            if array[m] < target:
                l = m + 1
            else:
                r = m
        return l
                
        
        
    def rightSearch(self, array, target):
        
        l = 0
        r = len(array)
        while l < r:
            m = (l+r) // 2
            if array[m] <= target:
                l = m + 1
            else:
                r = m
        return l
        
        


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)

