class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        cb = collections.Counter(barcodes)
        for kk,l in cb.most_common():
            out = [[kk] for _ in range(l)]
            break
        i = 0
        for k in cb:
            if k != kk:
                for v in range(cb[k]):
                    out[i%l].append(k)
                    i += 1
        output = []
        for o in out:
            output += o
        return output
