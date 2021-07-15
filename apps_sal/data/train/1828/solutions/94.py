class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        if len(barcodes) <= 1:
            return barcodes
        
        heap, res = [], []
        counter = collections.Counter(barcodes)
        for val, cnt in counter.items():
            heapq.heappush(heap, (-cnt, val))
        
        res = []
        while len(heap) > 1:
            cnt1, val1 = heapq.heappop(heap)
            cnt2, val2 = heapq.heappop(heap)
            res.extend([val1, val2])
            cnt1 += 1
            cnt2 += 1
            if cnt1: heapq.heappush(heap, (cnt1, val1))
            if cnt2: heapq.heappush(heap, (cnt2, val2))
        
        if heap:
            res.append(heap[0][1])
        return res 
