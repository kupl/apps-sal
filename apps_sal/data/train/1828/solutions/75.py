class Solution:

    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        c = Counter(barcodes)
        heap = []
        ans = []
        for (k, v) in c.items():
            heapq.heappush(heap, (-v, k))
        while heap:
            (most, d1) = heapq.heappop(heap)
            if ans and ans[-1] == d1:
                (more, d2) = heapq.heappop(heap)
                ans.append(d2)
                if more < -1:
                    heapq.heappush(heap, (more + 1, d2))
                heapq.heappush(heap, (most, d1))
                continue
            ans.append(d1)
            if most < -1:
                heapq.heappush(heap, (most + 1, d1))
        return ans
