class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        count = defaultdict(int)
        for i in barcodes:
            count[i] -= 1
        h = []
        for i in count:
            heappush(h, (count[i], i))
        # even
        out = [0 for _ in range(len(barcodes))]
        freq, code = heappop(h)
        for i in range(0, len(barcodes), 2):
            out[i] = code
            freq += 1
            if not freq and h:
                freq, code = heappop(h)

        if not freq and h:
            freq, code = heappop(h)

        # odd
        for i in range(1, len(barcodes), 2):
            out[i] = code
            freq += 1
            if not freq and h:
                freq, code = heappop(h)

        return out
