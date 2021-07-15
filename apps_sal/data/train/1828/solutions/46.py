class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        h=[]
        d=defaultdict(int)
        for ele in barcodes:
            d[ele]+=1
            
        for key, val in d.items():
            heappush(h, (-1*val, key))
        res=[]
        prev=()
        while h:
            ele=heappop(h)
            freq=ele[0]*-1
            res.append(ele[1])
            if prev!=():
                heappush(h, prev)
            if freq!=1:
                prev=(-1*(freq-1), ele[1])
            else:
                prev=()
        return res
