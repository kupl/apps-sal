class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        h=[]
        c=collections.Counter(barcodes)
        for i in c:
            heapq.heappush(h,(-c[i],i))
        res=[]
        if len(barcodes)<2:
            return str(barcodes[0])
        while h:
            val1,char1=heapq.heappop(h)
            char2=''
            if h:
                val2,char2=heapq.heappop(h)
            res.append(char1)
            res.append(char2)
            
            if val1*(-1) > 1:
                heapq.heappush(h,(val1+1,char1))
            if val2*(-1)>1:
                heapq.heappush(h,(val2+1,char2))
        return res                        
            
            
            

