class Solution:

    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        if not barcodes:
            return []
        res = [None] * len(barcodes)
        barCount = collections.defaultdict(int)
        for barcode in barcodes:
            barCount[barcode] += 1
        mostFreq = max(barCount, key=barCount.get)
        i = 0
        for _ in range(barCount[mostFreq]):
            res[i] = mostFreq
            i += 2
        if i >= len(barcodes):
            i = 1
        barSet = set(barcodes)
        barSet.remove(mostFreq)
        for key in barSet:
            if key == mostFreq:
                continue
            for _ in range(barCount[key]):
                res[i] = key
                i += 2
                if i >= len(barcodes):
                    i = 1
        return res
