class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        s = set()
        
        for k,v in list(count.items()):
            if v in s:
                return False
            else:
                s.add(v)
        return True
            
            

