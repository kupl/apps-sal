class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        barcodes.sort()
        n = len(barcodes)
        result = list()

        if n % 2 == 0:
            for x, y in zip(barcodes[:n // 2], barcodes[n // 2:]):
                result.extend([y, x])
        else:
            midVal = barcodes[n // 2]
            isAdded = False
            prev = -1
            for x, y in zip(barcodes[:n // 2], barcodes[n // 2 + 1:]):
                if isAdded == False and prev != midVal and y != midVal:
                    result.append(midVal)
                    isAdded = True
                result.extend([y, x])
                prev = x
            if isAdded == False:
                result.append(midVal)
        return result
