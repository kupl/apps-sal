class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter = collections.Counter(barcodes)
        data = [[] for i in range(len(barcodes) + 1)]

        for i in counter:
            data[counter[i]].append(i)

        res = [None for k in range(len(barcodes))]
        temp = 0
        for j in range(len(data) - 1, 0, -1):
            if len(data[j]) == 0:
                continue
            for char in data[j]:
                times = j
                while(times > 0):
                    res[temp] = char
                    temp += 2
                    times -= 1
                    if temp >= len(res):
                        temp = 1
        return res
