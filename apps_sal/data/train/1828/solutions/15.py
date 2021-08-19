class Solution:

    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        n = len(barcodes)
        counter = Counter(barcodes)
        sorted_barcodes = sorted(barcodes, key=lambda x: (counter[x], x))
        res = [0] * n
        (res[1::2], res[::2]) = (sorted_barcodes[:n // 2], sorted_barcodes[n // 2:])
        return res
