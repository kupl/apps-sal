class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        cnts = collections.defaultdict(int)
        for n in barcodes:
            cnts[n] += 1

        barcodes.sort(key=lambda x: (cnts[x], x))
        n = len(barcodes)
        first, second = barcodes[:n // 2], barcodes[n // 2:]
        res = []
        f, s = 0, 0
        while f < len(first) or s < len(second):
            if s < len(second):
                res.append(second[s])
                s += 1
            if f < len(first):
                res.append(first[f])
                f += 1
        return res
