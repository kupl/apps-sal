class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        count = {}
        for code in barcodes:
            if code in count:
                count[code] += 1
            else:
                count[code] = 1
        count = {k: v for k, v in sorted(count.items(), key=lambda item: item[1], reverse=True)}

        it = iter(count.keys())
        cur = next(it)
        i = 0
        while i < len(barcodes):
            while count[cur] == 0:
                cur = next(it)
            barcodes[i] = cur
            count[cur] -= 1
            i += 2
        i = 1
        while i < len(barcodes):
            while count[cur] == 0:
                cur = next(it)
            barcodes[i] = cur
            count[cur] -= 1
            i += 2
        return barcodes
