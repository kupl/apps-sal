import heapq
from collections import Counter


class Solution:

    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        c = Counter(barcodes)
        heap = []
        res = []
        for (key, val) in list(c.items()):
            heap.append((-val, key))
        heapq.heapify(heap)
        prevCnt = 0
        while heap:
            (cnt, code) = heapq.heappop(heap)
            cnt = -cnt
            res.append(code)
            if prevCnt > 0:
                heapq.heappush(heap, (-prevCnt, prevCode))
            prevCnt = cnt - 1
            prevCode = code
        return res
