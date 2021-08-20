from collections import Counter


class Solution:

    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freqs = Counter(barcodes)
        result = [-1] * len(barcodes)
        i = 0
        for (bc, c) in sorted(freqs.items(), key=lambda x: -x[1]):
            for _ in range(c):
                if i >= len(result):
                    i = 1
                result[i] = bc
                i += 2
        return result
