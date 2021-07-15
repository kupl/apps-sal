class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        max_v = max(len(barcodes), max(barcodes))+1
        freq = [0]*max_v
        for v in barcodes:
            freq[v]+=1
        sortedList=[[] for _ in range(max_v)]
        for v, f in enumerate(freq):
            if f > 0:
                sortedList[-f].extend([v]*f)
        result = []
        for index in sortedList:
            for mi in index:
                    result.append(mi)
        barcodes = result
        res = [\"\"]*len(barcodes)
        i = 0
        j = 0
        while j < len(barcodes):
            res[i] = barcodes[j]
            i=i+2
            j=j+1
            if i > len(res)-1:
                i=1
        return res
        
        
