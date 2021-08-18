from heapq import heappush, heappop, heapify


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:

        counter = Counter(barcodes)
        i = 0
        for n, count in counter.most_common():
            for _ in range(count):
                barcodes[i] = n
                i += 2
                if i >= len(barcodes):
                    i = 1
        return barcodes
