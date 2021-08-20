class Solution:

    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counts = {k: 0 for k in barcodes}
        for n in barcodes:
            counts[n] += 1
        barcodes.sort()
        barcode = []
        heap = [(-y, x) for (x, y) in list(counts.items())]
        heapq.heapify(heap)
        print(heap)
        while len(heap) > 0:
            (freq, digit) = heapq.heappop(heap)
            if len(barcode) == 0 or barcode[-1] != digit:
                barcode.append(digit)
                if freq < -1:
                    freq += 1
                    heapq.heappush(heap, (freq, digit))
            else:
                (nextFreq, nextDig) = heapq.heappop(heap)
                barcode.append(nextDig)
                heapq.heappush(heap, (freq, digit))
                if nextFreq < -1:
                    nextFreq += 1
                    heapq.heappush(heap, (nextFreq, nextDig))
        return barcode
