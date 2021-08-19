from heapq import heappush, heappop, heapify


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # 1. Heap: O(N log N) Time, O(N) Space
        #         counter = defaultdict(int)
        #         for n in barcodes:
        #             counter[n] += 1

        #         maxHeap = []
        #         for n, val in counter.items():
        #             heappush(maxHeap, [-val, n])

        #         prev = None
        #         for i in range(len(barcodes)):
        #             val, id = heappop(maxHeap)
        #             if val < 0:
        #                 temp = [val + 1, id]
        #             else:
        #                 temp = None

        #             barcodes[i] = id

        #             if prev:
        #                 heappush(maxHeap, prev)
        #             prev = temp
        #         return barcodes

        # 2. Bucket Sort
        counter = Counter(barcodes)
        i = 0
        for n, count in counter.most_common():
            for _ in range(count):
                barcodes[i] = n
                i += 2
                if i >= len(barcodes):
                    i = 1
        return barcodes
