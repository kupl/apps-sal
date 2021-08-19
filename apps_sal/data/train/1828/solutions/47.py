class Solution:

    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        hq = [(-v, i) for (i, v) in collections.Counter(barcodes).items()]
        heapq.heapify(hq)
        res = []
        while hq:
            temp = []
            for _ in range(min(len(hq), 2)):
                (val, number) = heapq.heappop(hq)
                temp.append((val, number))
                res.append(number)
            for _ in range(len(temp)):
                (val, number) = temp.pop()
                if val < -1:
                    heapq.heappush(hq, (val + 1, number))
        return res
