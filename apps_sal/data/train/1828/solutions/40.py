import heapq
from collections import Counter

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counts = Counter(barcodes)
        arr = [[-v, k] for k, v in list(counts.items())]
        heapq.heapify(arr)
        newBarcodes = []
        while len(arr) != 0:
            elem1 = heapq.heappop(arr)
            newBarcodes.append(elem1[1])
            if len(arr) == 0:
                return newBarcodes
            elem2 = heapq.heappop(arr)
            newBarcodes.append(elem2[1])
            elem1[0] += 1
            if elem1[0] < 0:
                heapq.heappush(arr, elem1)
            elem2[0] += 1
            if elem2[0] < 0:
                heapq.heappush(arr, elem2)
        return newBarcodes
            

