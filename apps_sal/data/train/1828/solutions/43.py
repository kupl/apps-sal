class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        if len(barcodes) < 2:
            return barcodes

        counter = collections.Counter(barcodes)

        heap = []

        for k, v in counter.items():
            heapq.heappush(heap, (-v, k))
        result = []
        while len(heap) > 1:
            count1, key1 = heapq.heappop(heap)
            count2, key2 = heapq.heappop(heap)
            result.append(key1)
            result.append(key2)
            count1 += 1
            count2 += 1
            if count1 < 0:
                heapq.heappush(heap, (count1, key1))
            if count2 < 0:
                heapq.heappush(heap, (count2, key2))

        print(heap)
        if len(heap) > 0:
            count, key = heapq.heappop(heap)
            result.append(key)
            return result
        else:
            return result
