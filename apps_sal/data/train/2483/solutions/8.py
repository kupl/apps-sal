class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occd = {}
        for n in arr:
            if n in occd:
                occd[n] += 1
            else:
                occd[n] = 1
                
        s = set()
        for k, v in occd.items():
            if v in s:
                return False
            s.add(v)
            
        return True
