from collections import Counter
import heapq


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:

        count = Counter(barcodes)
        pq = []

        for tup in count.items():
            heapq.heappush(pq, (-tup[1], tup[0]))

        res = []

        prev_freq, prev_char = 0, None

        while pq:

            freq, num = heapq.heappop(pq)

            if -prev_freq > 0 and prev_char:
                heapq.heappush(pq, (prev_freq, prev_char))

            res.append(num)
            prev_freq = freq + 1
            prev_char = num

        return res
