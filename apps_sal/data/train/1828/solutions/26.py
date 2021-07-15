from collections import Counter
import heapq as q

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        c = Counter(barcodes)
        
        xs = []
        for k, v in list(c.items()):
            q.heappush(xs, (-v, k))
        
        r = []
        while len(xs) > 1:
            av, ak = q.heappop(xs)
            bv, bk = q.heappop(xs)
            
            r.append(ak)
            r.append(bk)
            
            av += 1
            bv += 1
            if av < 0:
                q.heappush(xs, (av, ak))
            if bv < 0:
                q.heappush(xs, (bv, bk))
        
        
        if len(xs) == 0: return r
        
        av, ak = q.heappop(xs)
        
        r.append(ak)
        
        return r
        

