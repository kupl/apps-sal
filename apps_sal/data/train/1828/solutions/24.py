class Solution:

    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        m = [0 for _ in range(10001)]
        max_cnt = 0
        max_n = 0
        for n in barcodes:
            m[n] += 1
            if m[n] > max_cnt:
                max_cnt = m[n]
                max_n = n
        res = [0 for _ in range(len(barcodes))]
        pos = 0
        for i in range(10001):
            n = max_n if i == 0 else i
            while m[n] > 0:
                m[n] -= 1
                res[pos] = n
                pos = pos + 2 if pos + 2 < len(barcodes) else 1
        return res
