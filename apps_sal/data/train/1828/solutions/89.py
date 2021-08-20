from collections import Counter


class Solution:

    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counts = Counter(barcodes)
        n = len(barcodes)
        res = [0] * n
        i = 0
        for (k, v) in counts.most_common():
            while v > 0:
                res[i] = k
                i += 2
                v -= 1
                if i > n - 1:
                    i = 1
        return res
