from collections import Counter, deque
from heapq import *


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        count = Counter(barcodes)
        res = []
        maxHeap = []
        for num, freq in list(count.items()):
            heappush(maxHeap, (-freq, num))
        q = deque([])
        while maxHeap:
            negCnt, num = heappop(maxHeap)
            res.append(num)

            q.append((negCnt, num))
            if len(q) == 2:
                negCnt, num = q.popleft()
                negCnt += 1
                if negCnt < 0:
                    heappush(maxHeap, (negCnt, num))

        return res
