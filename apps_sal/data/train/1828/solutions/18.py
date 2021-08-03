class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        record = dict()
        for bar in barcodes:
            record[bar] = record.get(bar, 0) + 1
        record = sorted([(k, v) for k, v in record.items()], key=lambda x: x[1], reverse=True)
        max_count = record[0][1]
        read = []
        for k, v in record:
            read += [k] * v
        L = len(read)
        res = [[] for _ in range(max_count)]
        for idx in range(L):
            res[idx % max_count].append(read[idx])
        ress = []
        for r in res:
            ress += r
        return ress
