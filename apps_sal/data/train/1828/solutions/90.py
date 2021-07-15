from collections import Counter
import itertools
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        barcodes = [(freq, k) for k, freq in Counter(barcodes).items()]
        barcodes.sort(reverse=True)
        barcodes = list(itertools.chain.from_iterable([[k]*f for f, k in barcodes]))
        res=[\"\"]*len(barcodes)
        i = 0
        j = 0
        while j < len(barcodes):
            res[i] = barcodes[j]
            i=i+2
            j=j+1
            if i > len(res)-1:
                i=1
        return res
        
        
