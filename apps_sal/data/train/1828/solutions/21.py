class Solution:

    def rearrangeBarcodes(self, barcodes):
        cnt = dict()
        for v in barcodes:
            cnt[v] = cnt.get(v, 0) + 1
        N = len(barcodes)
        barcodes.sort(key=lambda v: (cnt[v], v), reverse=True)
        A = [0] * N
        (A[::2], A[1::2]) = (barcodes[:(N + 1) // 2], barcodes[(N + 1) // 2:])
        return A
