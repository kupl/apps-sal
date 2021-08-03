class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter = Counter(barcodes)
        heap = [(-v, c) for c, v in counter.items()]
        heapq.heapify(heap)
        res = []
        while heap:
            popped = []
            for _ in range(2):
                if not heap:
                    return res
                v, c = heapq.heappop(heap)
                res.append(c)
                if v < -1:
                    popped.append([v + 1, c])

            for v, c in popped:
                heapq.heappush(heap, (v, c))

        return res
