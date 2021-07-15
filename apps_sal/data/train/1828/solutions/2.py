from collections import Counter
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        barcodes = Counter(barcodes)
        a = []
        for i,j in barcodes.most_common():
            a.extend([i]*j)
        l = len(a)
        res = [0]*l
        j=0
        for i in range(0,l,2):
            res[i]=a[j]
            j+=1
        for i in range(1,l,2):
            res[i]=a[j]
            j+=1
        return res
            

