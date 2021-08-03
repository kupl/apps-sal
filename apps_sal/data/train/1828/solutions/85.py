class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter_dict = collections.Counter(barcodes)
        kk_heap = []
        for it in list(counter_dict.items()):
            heapq.heappush(kk_heap, [-it[1], it[0]])

        last_kk = None
        res = []

        while kk_heap:
            if len(kk_heap) == 1:
                res.append(kk_heap[0][1])
                break

            choose_from = [heapq.heappop(kk_heap), heapq.heappop(kk_heap)]
            idx = 0 if last_kk != choose_from[0][1] else 1
            kk = choose_from[idx][1]

            res.append(kk)
            choose_from[idx][0] += 1
            for cf in choose_from:
                if cf[0]:
                    heapq.heappush(kk_heap, cf)
            last_kk = kk

        return res
