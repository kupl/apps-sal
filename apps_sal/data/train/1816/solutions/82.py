from collections import Counter
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        times = sorted(enumerate(keyTime), key= lambda x: (int(x[1].split(\":\")[0]), int(x[1].split(\":\")[1])))
        
        def isValid(time1, time2):
            h1, m1 = time1.split(\":\")
            h2, m2 = time2.split(\":\")
            if h1 == h2: return True
            if int(h2) - int(h1) > 1:
                return False    
            if (60 - int(m1)) + int(m2) > 60:
                return False
            
            return True
        start = 0
        res = set()
        end = 0
        cache = Counter()
        while start < len(times):
            while end < len(times) and isValid(times[start][1], times[end][1]):
                cache[keyName[times[end][0]]] += 1
                if cache[keyName[times[end][0]]] >= 3:
                    res.add(keyName[times[end][0]])
                end += 1
            cache[keyName[times[start][0]]] -= 1
            if cache[keyName[times[start][0]]] == 0: 
                del cache[keyName[times[start][0]]] 
            start += 1
        return sorted(res)
                
   
        
        
        
