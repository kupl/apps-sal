class Solution:

    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        import heapq
        from collections import Counter
        cnt = Counter(barcodes)
        items = [(-v, k) for (k, v) in cnt.items()]
        heapq.heapify(items)
        res = []
        while len(items) > 1:
            (v1, k1) = heapq.heappop(items)
            v1 += 1
            (v2, k2) = heapq.heappop(items)
            v2 += 1
            res.extend([k1, k2])
            if v1 != 0:
                heapq.heappush(items, (v1, k1))
            if v2 != 0:
                heapq.heappush(items, (v2, k2))
        if len(items) == 1:
            res.append(items[0][1])
        return res
