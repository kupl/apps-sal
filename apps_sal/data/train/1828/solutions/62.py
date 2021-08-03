import heapq
from collections import Counter


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        ans = []
        c = Counter(barcodes)
        heap = []
        for b in c:
            heapq.heappush(heap, (-c[b], b))
        while(heap):
            temp = heapq.heappop(heap)
            if(ans and ans[-1] == temp[1]):
                temp2 = heapq.heappop(heap)
                ans.append(temp2[1])
                heapq.heappush(heap, (temp[0], temp[1]))
                if(temp2[0] < -1):
                    heapq.heappush(heap, (temp2[0] + 1, temp2[1]))
            else:
                ans.append(temp[1])
                if(temp[0] < -1):
                    heapq.heappush(heap, (temp[0] + 1, temp[1]))
        return ans
