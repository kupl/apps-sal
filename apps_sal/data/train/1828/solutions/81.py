class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:

        count = Counter(barcodes)
        pq = []
        for c in count:
            heappush(pq, [-count[c], c])
        output = []
        prev = None

        while pq:

            c, v = heappop(pq)
            c += 1
            output.append(v)

            if prev:
                heappush(pq, prev)
                prev = None

            if c != 0:
                prev = [c, v]

        return output
