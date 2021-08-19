class Solution:

    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freq = collections.Counter(barcodes)
        heap = []
        for (k, v) in freq.items():
            heapq.heappush(heap, (-v, k))
        ans = []
        while heap:
            (freq, num) = heapq.heappop(heap)
            if not ans:
                ans.append(num)
                freq += 1
                if freq < 0:
                    heapq.heappush(heap, (freq, num))
            elif num == ans[-1]:
                (nextFreq, nextNum) = heapq.heappop(heap)
                ans.append(nextNum)
                nextFreq += 1
                if nextFreq < 0:
                    heapq.heappush(heap, (nextFreq, nextNum))
                heapq.heappush(heap, (freq, num))
            else:
                ans.append(num)
                freq += 1
                if freq < 0:
                    heapq.heappush(heap, (freq, num))
        return ans
