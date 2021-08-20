from heapq import heappush, heappop
from collections import defaultdict


class Solution:

    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freq = defaultdict(int)
        for code in barcodes:
            freq[code] += 1
        (maxH, res) = ([], [])
        for (num, count) in freq.items():
            heappush(maxH, (-count, num))
        while maxH:
            (count1, num1) = heappop(maxH)
            count1 += 1
            res.append(num1)
            if maxH:
                (count2, num2) = heappop(maxH)
                res.append(num2)
                count2 += 1
                if count2 < 0:
                    heappush(maxH, (count2, num2))
            if count1 < 0:
                heappush(maxH, (count1, num1))
        return res
