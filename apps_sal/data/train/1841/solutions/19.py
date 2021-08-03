class Solution:
    def get_median(self, arr):
        arr.sort()
        n = len(arr)

        return arr[(n - 1) // 2]

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        StrengthIndexAndVal = collections.namedtuple('StrengthIndexAndVal', ('strength', 'index', 'val'))

        if len(arr) == 0:
            return []

        m = self.get_median(arr)
        heap = []
        for i, val in enumerate(arr):
            siv = StrengthIndexAndVal(abs(val - m), i, val)
            if len(heap) == k:
                heapq.heappushpop(heap, siv)
            else:
                heapq.heappush(heap, siv)

        return [x.val for x in heap]
