class Solution:

    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        dt = collections.Counter(barcodes)
        hp = []
        for (code, freq) in list(dt.items()):
            heapq.heappush(hp, (-freq, code))
        res = []
        while len(hp) > 1:
            (freq1, bar1) = heapq.heappop(hp)
            (freq2, bar2) = heapq.heappop(hp)
            res.append(bar1)
            res.append(bar2)
            if freq1 < -1:
                heapq.heappush(hp, (freq1 + 1, bar1))
            if freq2 < -1:
                heapq.heappush(hp, (freq2 + 1, bar2))
        if hp:
            res.append(heapq.heappop(hp)[1])
        return res
