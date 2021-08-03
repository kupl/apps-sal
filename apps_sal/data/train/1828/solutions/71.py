class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        d = defaultdict(lambda: 0)
        for b in barcodes:
            d[b] += 1

        #heap = [(d[b],b) for b in barcodes]
        counter = 0
        heap = []
        for b in d:
            heap.append((-d[b], counter, b))
            counter += 1
        heapify(heap)
        result = []
        while heap:
            count1, tmp, b1 = heappop(heap)
            result.append(b1)
            if not heap:
                return result

            count2, tmp, b2 = heappop(heap)
            result.append(b2)

            count1 += 1
            count2 += 1

            if count1:
                heappush(heap, (count1, counter, b1))
                counter += 1
            if count2:
                heappush(heap, (count2, counter, b2))
                counter += 1
        return result
