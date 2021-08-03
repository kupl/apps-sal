class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        import heapq
        from collections import defaultdict

        d = defaultdict(int)

        for i in barcodes:
            d[i] += 1
        h = []
        for i in d:
            h.append((-d[i], i))
        heapq.heapify(h)
        ans = []

        while(len(h) > 1):
            c1, val1 = heapq.heappop(h)
            c2, val2 = heapq.heappop(h)

            c1 += 1
            c2 += 1

            ans.append(val1)
            ans.append(val2)

            if c1:
                heapq.heappush(h, (c1, val1))
            if c2:
                heapq.heappush(h, (c2, val2))

        if h:
            ans.append(heapq.heappop(h)[1])

        return ans
