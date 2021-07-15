class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        
        d = Counter(barcodes)
        cand = barcodes[0]
        maxi = d[cand]
        
        for idx,(k,v) in enumerate(d.items()):
            
            if v > maxi:
                maxi = v
                cand = k
        
        res =[None for i in range(len(barcodes))]
        pos = 0
        for i in range(maxi):
            res[pos] = cand
            pos+=2
        
        del d[cand]
        
        for idx,(k,v) in enumerate(d.items()):
            
            for j in range(v):
                if pos >= len(res):
                    pos = 1
                    
                res[pos] = k
                pos+=2
        
        return res
                
            
            
        

