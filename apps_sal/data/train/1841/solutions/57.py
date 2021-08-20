import heapq


class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        index = len(arr) // 2 - (1 - len(arr) % 2)
        median = sorted(arr)[index]
        heap = []
        for (i, el) in enumerate(arr):
            heapq.heappush(heap, (-abs(el - median), -el))
        els = heapq.nsmallest(k, heap, key=lambda x: (x[0], x[1]))
        return [-el[1] for el in els]
