from collections import Counter
from heapq import heapify, heappop
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        c = Counter(barcodes)
        h = []
        for k, count in list(c.items()):
            h.append((-count, k))
        heapify(h)
        
        res = [0] * len(barcodes)
        index = 0
        while h:
            count, num = heappop(h)
            count = -count
            while count:
                if index >= len(barcodes):
                    index = 1
                res[index] = num
                index += 2
                count -= 1
        return res

