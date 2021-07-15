import heapq as hq
from collections import Counter

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter = Counter(barcodes)
        cqueue = [(-v, k) for k, v in list(counter.items())]
        hq.heapify(cqueue)
        res = []
        while len(cqueue) > 0:
            neg_count, barcode = hq.heappop(cqueue)

            if len(res) != 0 and res[-1] == barcode:
                neg_count_2, barcode_2 = hq.heappop(cqueue)
                hq.heappush(cqueue, (neg_count, barcode))
                neg_count, barcode = neg_count_2, barcode_2
            res.append(barcode)

            if neg_count != -1:
                hq.heappush(cqueue, (neg_count + 1, barcode))
        
        return res
                
        

