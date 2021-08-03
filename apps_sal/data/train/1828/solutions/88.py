class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:

        cnts = collections.Counter(barcodes)
        heap = [(-v, k) for k, v in cnts.items()]
        heapq.heapify(heap)
        res = []

        while heap:
            cnt1, num1 = heapq.heappop(heap)
            if res and res[-1] == num1:
                cnt, num = heapq.heappop(heap)
                res.append(num)
                cnt += 1
                if cnt != 0:
                    heapq.heappush(heap, (cnt, num))
                heapq.heappush(heap, (cnt1, num1))
            else:
                res.append(num1)
                cnt1 += 1
                if cnt1 != 0:
                    heapq.heappush(heap, (cnt1, num1))

        return res
