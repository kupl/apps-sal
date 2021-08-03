from collections import defaultdict
import heapq


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        d = defaultdict(int)
        heap = []
        res = []
        for bc in barcodes:
            d[bc] += 1

        for key, val in d.items():
            heapq.heappush(heap, (-val, key))
        while heap:
            cur = heapq.heappop(heap)
            if res and res[-1] == cur[1]:
                tmp = heapq.heappop(heap)
                res.append(tmp[1])
                val = 1 + tmp[0]
                if val != 0:
                    heapq.heappush(heap, (val, tmp[1]))
                heapq.heappush(heap, (cur))

            else:
                res.append(cur[1])
                v = cur[0] + 1
                if v != 0:
                    heapq.heappush(heap, (v, cur[1]))
        return res
