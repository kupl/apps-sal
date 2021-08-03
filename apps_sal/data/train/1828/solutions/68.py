import heapq
from collections import Counter


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        maxheap = []
        K = 0
        map1 = Counter(barcodes)
        index = 0
        for k, v in list(map1.items()):
            heappush(maxheap, (-v, k))

        res = [0] * len(barcodes)
        while len(maxheap) > 0:

            element = heappop(maxheap)

            res[index] = element[1]
            if len(maxheap) == 0:
                break
            index += 1

            element2 = heappop(maxheap)

            res[index] = element2[1]

            self.updateMap(map1, maxheap, element)
            self.updateMap(map1, maxheap, element2)

            index += 1
        return res

    def updateMap(self, map1, maxheap, element):
        if map1[element[1]] == 1:
            del map1[element[1]]
        else:
            map1[element[1]] = map1[element[1]] - 1

            heappush(maxheap, (-map1[element[1]], element[1]))
