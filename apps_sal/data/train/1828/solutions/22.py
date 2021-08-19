class Solution:

    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        count = collections.Counter(barcodes)
        barcodes.sort(key=lambda a: (count[a], a))
        (barcodes[1::2], barcodes[::2]) = (barcodes[0:len(barcodes) // 2], barcodes[len(barcodes) // 2:])
        return barcodes
